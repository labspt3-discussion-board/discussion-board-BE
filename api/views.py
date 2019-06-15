
# region
from rest_framework                  import status
from rest_framework.parsers          import JSONParser
from rest_framework.views            import APIView
from rest_framework.response         import Response
from rest_framework                  import generics
from django.views.decorators.csrf    import csrf_exempt
from django.shortcuts                import render
from django.http                     import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core                     import serializers
from django.contrib.auth.models      import User
from django.contrib.auth             import get_user_model
from django.db.models                import Count
from django.contrib.auth             import get_user_model, authenticate, login, logout
from api.models                      import Subforum, Discussion, Comments, UserToSubforum
from api.serializers                 import UserSerializer, SubforumSerializer, DiscussionSerializer, CommentSerializer, UserToSubforumSerializer
from django.conf                     import settings
from validate_email                  import validate_email
from django.middleware.csrf          import get_token
from dotenv                          import load_dotenv
from rest_framework.authtoken.views  import ObtainAuthToken
from rest_framework.authtoken.models import Token
import os
import json
import requests
import random
# endregion

# GOOGLE_AUTH_REDIRECT_URI = 'http://localhost:8000/api/users/oauth/google/'
GOOGLE_AUTH_REDIRECT_URI = 'https://discussion-board-api-test.herokuapp.com/api/users/oauth/google/'
FACEBOOK_AUTH_REDIRECT_URI = 'https://discussion-board-api-test.herokuapp.com/api/users/oauth/facebook/'
# CLIENT_APP_URL = 'http://localhost:3000/'
CLIENT_APP_URL = 'https://lambda-discussion-board-test.herokuapp.com/'

# /api/
class Index(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated:
            User = get_user_model()
            users = User.objects.all()
            user_serializer = UserSerializer(users, many=True)
            return Response(user_serializer.data)
        else:
            response = HttpResponse(status=403)
            return response

# /api/users/login/check/
class UserLoginCheck(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            User = request.user
            user_serializer = UserSerializer(User, many=False)
            info            = user_serializer.data

            data = {
                'user': {
                    'id':         info['id'],
                    'username':   info['username'],
                    'email':      info['email'],
                    'first_name': info['first_name'],
                    'last_name':  info['last_name'],
                    'premium':    info['premium'],
                    'created_at': info['created_at'],
                    'subforums':  info['subforums'],
                    'avatar_img': '',
                },
            }
            return Response(data)

# /api/users/login/
class UserLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():

            # Get token and user
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            User = get_user_model()

            # Get user data
            user            = User.objects.get(id=user.pk)
            user_serializer = UserSerializer(user, many=False)
            info            = user_serializer.data

            data = {
                'user': {
                    'id':         info['id'],
                    'username':   info['username'],
                    'email':      info['email'],
                    'first_name': info['first_name'],
                    'last_name':  info['last_name'],
                    'premium':    info['premium'],
                    'created_at': info['created_at'],
                    'subforums':  info['subforums'],
                    'avatar_img': '',
                },
                'token': token.key,
            }

            return Response(data)
        else:
            return Response({'Error': 'Invalid Credentials'})

        # serializer.is_valid(raise_exception=True)

# /api/users/register/
class UserRegister(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        data = JSONParser().parse(request)
        User = get_user_model()

        # Validate username
        username = ''
        if data['username'] is not None:
            username = data['username']
        else:
            return Response('Missing username property')

        # Validate email
        email = ''
        if data['email'] is not None:
            email = data['email']
            if validate_email(email) is not True:
                return Response('Invalid email')
        else:
            return Response('Missing email property')

        email      = data['email']
        password   = data['password']
        first_name = data['firstName']
        last_name  = data['lastName']

        # Create user
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        user.save()

        data = {
            "username": email,
            "password": password
        }

        serializer = self.serializer_class(data=data, context={'request': request})

        if serializer.is_valid():

            # Get token and user
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            User = get_user_model()

            # Get user data
            user            = User.objects.get(id=user.pk)
            user_serializer = UserSerializer(user, many=False)
            info            = user_serializer.data

            data = {
                'user': {
                    'id':         info['id'],
                    'username':   info['username'],
                    'email':      info['email'],
                    'first_name': info['first_name'],
                    'last_name':  info['last_name'],
                    'premium':    info['premium'],
                    'created_at': info['created_at'],
                    'subforums':  info['subforums'],
                },
                'token': token.key,
            }

            return Response(data)
        else:
            return Response({'Error': 'There was an error'})

# /api/users/logout/
class UserLogout(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({ 'Success': 'Successfully logged out' })
        else:
            return HttpResponse({ 'Error': 'There was an error' }, status=status.HTTP_400_BAD_REQUEST)

# /api/users/oauth/google/
class UserOauthGoogle(APIView):
    def get(self, request, format=None):

        code = request.query_params.get('code','')

        # Get the token url and user info url from the discovery document.
        url_req = requests.get('https://accounts.google.com/.well-known/openid-configuration')
        token_endpoint = url_req.json()['token_endpoint']
        userinfo_endpoint = url_req.json()['userinfo_endpoint']

        # Exchange code for access token and id token
        data = {
            'code': code,
            'client_id': str(os.environ.get('GOOGLE_OAUTH_ID')),
            'client_secret': str(os.environ.get('GOOGLE_OAUTH_SECRET')),
            'redirect_uri': GOOGLE_AUTH_REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
        token_req = requests.post(token_endpoint, data)
        access_token = token_req.json()['access_token']
        id_token = token_req.json()['id_token']

        # Get user info
        headers = { 'Authorization': str('Bearer ' + access_token) }
        info_req = requests.get(userinfo_endpoint, headers=headers)

        user_info = info_req.json()

        first_name = user_info['given_name']
        last_name  = user_info['family_name']
        email      = user_info['email']
        username   = first_name.lower() + '.' + last_name.lower() + str(random.randint(0,1001))
        avatar_img = user_info['picture']
        auth_type  = 'oauth'

        # Create/login user
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except get_user_model().DoesNotExist:
            user = User.objects.create_user(username, email, first_name=first_name, last_name=last_name, auth_type=auth_type)

        token, created = Token.objects.get_or_create(user=user)

        user_serializer = UserSerializer(user, many=False)

        if user_serializer.data['auth_type'] == auth_type:            
            response = HttpResponseRedirect(CLIENT_APP_URL + '?token=' + str(token.key) + '&loggedIn=true&avatarImg=' + str(avatar_img))
            return response
        else:
            response = HttpResponseRedirect(CLIENT_APP_URL + '?loggedIn=false')
            return response

# /api/users/oauth/facebook/
class UserOauthFacebook(APIView):
    def get(self, request, format=None):

        code = request.query_params.get('code','')

        # Get access token
        url = 'https://graph.facebook.com/v3.3/oauth/access_token?client_id=' + str(os.environ.get('FACEBOOK_OAUTH_ID')) + '&redirect_uri=' + FACEBOOK_AUTH_REDIRECT_URI + '&client_secret=' + str(os.environ.get('FACEBOOK_OAUTH_SECRET')) + '&code=' + code

        token_req = requests.get(url)
        access_token = token_req.json()['access_token']

        # Get user info
        info_req = requests.get('https://graph.facebook.com/me?access_token=' + str(access_token) + '&fields=first_name,last_name,email')

        user_info = info_req.json()

        user_id    = user_info['id']
        first_name = user_info['first_name']
        last_name  = user_info['last_name']
        email      = user_info['email']
        username   = first_name.lower() + '.' + last_name.lower() + str(random.randint(0,1001))
        auth_type  = 'oauth'

        # Get avatar image.
        pic_req = requests.get('https://graph.facebook.com/' + user_id + '/picture')
        # avatar_img = pic_req.json()


        return Response(user_info)

        # Create/login user
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except get_user_model().DoesNotExist:
            user = User.objects.create_user(username, email, first_name=first_name, last_name=last_name, auth_type=auth_type)

        user_serializer = UserSerializer(user, many=False)

        if user_serializer.data['auth_type'] == auth_type:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            response = HttpResponseRedirect(CLIENT_APP_URL + '?id=' + str(user_serializer.data['id']) + '&loggedIn=true')
            return response
        else:
            response = HttpResponseRedirect(CLIENT_APP_URL + '?loggedIn=false')
            return response

# /api/users/
class UserList(APIView):

    def get(self, request, format=None):
        User            = get_user_model()
        users           = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)

# /api/users/:id
class UserDetails(APIView):

    def get_object(self, id):

        try:
            return get_user_model().objects.get(id=id)
        except get_user_model().DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):

        user = self.get_object(uuid)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    def put(self, request, uuid, format=None):

        data = JSONParser().parse(request)
        user = self.get_object(uuid)
        user_serializer = UserSerializer(user, data=data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):

        user = self.get_object(uuid)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# /api/subforums/
class SubforumList(APIView):

    def get(self, request, format=None):
        return Response(request.COOKIES)
 

# /api/Subforums/:uuid
class SubforumDetails(APIView):
    def get_object(self, id):

        try:
            return Subforum.objects.get(uuid=uuid)
        except Subforum.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):

        Subforum = self.get_object(id)
        Subforum_serializer = SubforumSerializer(Subforum)
        return Response(Subforum_serializer.data)

    def put(self, request, id, format=None):

        data = JSONParser().parse(request)
        Subforum = self.get_object(uuid)
        Subforum_serializer = SubforumSerializer(Subforum, data=data)

        if Subforum_serializer.is_valid():
            Subforum_serializer.save()
            return Response(Subforum_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):

        Subforum = self.get_object(id)
        Subforum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# /api/subtopics/id/users
# /api/subtopics/id/discussions
class SubforumDiscussions(generics.ListAPIView):
    serializer_class = DiscussionSerializer
    lookup_url_kwarg = 'id'

    def get_object(self, id):
        try:
            return Subforum.objects.get(id=id)
        except Subforum.DoesNotExist:
            raise Http404

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        subforum = self.get_object(id)
        if subforum:
            discussion = Discussion.objects.filter(subtopic=id)
            return discussion

# /api/discussions/
class DiscussionList(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

# /api/discussions/id/
class DiscussionDetails(APIView):
    def get_object(self, id):

        try:
            return Discussion.objects.get(id=id)
        except Discussion.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        discussion = self.get_object(id)
        discussion_serializer = DiscussionSerializer(discussion)
        return Response(discussion_serializer.data)

    def put(self, request, id, format=None):

        data = JSONParser().parse(request)
        discussion = self.get_object(id)
        discussion_serializer = DiscussionSerializer(discussion, data=data)

        if discussion_serializer.is_valid():
            discussion_serializer.save()
            return Response(discussion_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):

        discussion = self.get_object(id)
        discussion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# /api/discussions/id/comments
class DiscussionComments(generics.ListAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'id'

    def get_object(self, id):
        try:
            return Discussion.objects.get(id=id)
        except Discussion.DoesNotExist:
            raise Http404

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        discussion = self.get_object(id)
        if discussion:
            comments = Comments.objects.filter(discussion_id=id)
            return comments

# /api/topdiscussions/
class TopDiscussions(generics.ListAPIView):
    queryset = Discussion.objects.annotate(Count('upvote')).order_by('-upvote')
    serializer_class = DiscussionSerializer

# /api/comments/
class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

# /api/comments/id/
class CommentDetails(APIView):
    def get_object(self, id):

        try:
            return Comments.objects.get(id=id)
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        comment = self.get_object(id)
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data)

    def put(self, request, id, format=None):

        data = JSONParser().parse(request)
        comment = self.get_object(id)
        comment_serializer = CommentSerializer(comment, data=data)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):

        comment = self.get_object(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserToSubforumList(generics.ListCreateAPIView):
    queryset = UserToSubforum.objects.all()
    serializer_class = UserToSubforumSerializer
