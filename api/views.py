from rest_framework               import status
from rest_framework.parsers       import JSONParser
from rest_framework.views         import APIView
from rest_framework.response      import Response
from rest_framework               import generics
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts             import render
from django.http                  import HttpResponse, JsonResponse, Http404
from django.core                  import serializers
from django.contrib.auth.models   import User
from django.contrib.auth          import get_user_model
from api.models                   import Subtopic, Discussion, Comments
from api.serializers              import UserSerializer, SubtopicSerializer, DiscussionSerializer, CommentSerializer
from django.conf                  import settings
import json
import uuid


# /api/
class Index(APIView):

    def get(self, request, format=None):
        Auth_User        = get_user_model()
        users            = Auth_User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)

# /api/users/
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    """def get(self, request, format=None):
        users           = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)

    def post(self, request, format=None):
        data            = JSONParser().parse(request)
        data['uuid']    = uuid.uuid4().hex            # Generate a random hexadecimal uuid for the new user
        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():
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
