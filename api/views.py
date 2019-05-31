from rest_framework               import status
from rest_framework.parsers       import JSONParser
from rest_framework.views         import APIView
from rest_framework.response      import Response
from rest_framework               import generics
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts             import render
from django.http                  import HttpResponse, JsonResponse, Http404
from django.core                  import serializers
# from django.contrib.auth.models   import User
from django.contrib.auth          import get_user_model, authenticate, login, logout
from api.models                   import Subtopic, Discussion, Comments
from api.serializers              import UserSerializer, SubtopicSerializer, DiscussionSerializer, CommentSerializer
from django.conf                  import settings
import json
import uuid


# /api/
class Index(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated:
            users = User.objects.all()
            user_serializer = UserSerializer(users, many=True)
            return Response(user_serializer.data)
        else:
            response = HttpResponse(status=403)
            return response

# /api/users/login/
class UserLogin(APIView):
    def post(self, request, format=None):
        data     = JSONParser().parse(request)
        email    = data['email']
        password = data['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            user_serializer = UserSerializer(user, many=False)
            return Response(user_serializer.data)
        else:
            return Response('nope')

# /api/users/logout/
class UserLogout(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response()

# /api/users/
class UserList(APIView):

    def get(self, request, format=None):
        User = get_user_model()
        users           = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        User = get_user_model()

        username   = data['username']
        email      = data['email']
        password   = data['password']
        first_name = data['firstName']
        last_name  = data['lastName']

        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        user.save()

        # login(request, user)

        # user_serializer = UserSerializer(user, many=False)

        # return Response(user_serializer, status=HTTP_201_CREATED)
        return Response()





        # data['uuid']    = uuid.uuid4().hex            # Generate a random hexadecimal uuid for the new user
        # user_serializer = UserSerializer(data=data)

        """if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

# /api/users/:uuid
class UserDetails(APIView):
    
    def get_object(self, uuid):

        try:
            return get_user_model().objects.get(uuid=uuid)
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

# /api/subtopics/
class SubtopicList(generics.ListCreateAPIView):
    queryset = Subtopic.objects.all()
    serializer_class = SubtopicSerializer

# /api/subtopics/:uuid
class SubtopicDetails(APIView):
    def get_object(self, uuid):

        try:
            return Subtopic.objects.get(uuid=uuid)
        except Subtopic.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):

        subtopic = self.get_object(uuid)
        subtopic_serializer = SubtopicSerializer(subtopic)
        return Response(subtopic_serializer.data)

    def put(self, request, uuid, format=None):

        data = JSONParser().parse(request)
        subtopic = self.get_object(uuid)
        subtopic_serializer = SubtopicSerializer(subtopic, data=data)

        if subtopic_serializer.is_valid():
            subtopic_serializer.save()
            return Response(subtopic_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):

        subtopic = self.get_object(uuid)
        subtopic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
