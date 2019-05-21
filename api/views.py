from rest_framework               import status
from rest_framework.parsers       import JSONParser
from rest_framework.views         import APIView
from rest_framework.response      import Response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts             import render
from django.http                  import HttpResponse, JsonResponse, Http404
from django.core                  import serializers
from django.contrib.auth.models   import User
from django.contrib.auth          import get_user_model
from api.models                   import Subtopic
from api.serializers              import UserSerializer
from django.conf                  import settings
import json
import uuid


# /api/ #
class Index(APIView):

    def get(self, request, format=None):
        Auth_User             = get_user_model()
        users            = Auth_User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)

# /api/users/
class UserList(APIView):

    def get(self, request, format=None):
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
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/users/:uuid
class UserDetails(APIView):

    def get_object(self, uuid):

        try:
            return settings.AUTH_USER_MODEL.objects.get(uuid=uuid)
        except settings.AUTH_USER_MODEL.DoesNotExist:
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
# class SubtopicList(APIView):
