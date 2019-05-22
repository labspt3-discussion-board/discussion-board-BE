from rest_framework             import serializers
from django.contrib.auth.models import User
from api.models                 import Subtopic
from django.conf                import settings
from django.contrib.auth        import get_user_model

class SubtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = ('id', 'uuid', 'name', 'private', 'created_at', 'owner')

class UserSerializer(serializers.ModelSerializer):
    subtopic = SubtopicSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = get_user_model()
        fields = ('id', 'uuid', 'username', 'email', 'password', 'premium', 'created_at', 'subtopic')
