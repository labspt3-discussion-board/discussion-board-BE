from rest_framework             import serializers
from django.contrib.auth.models import User
from api.models                 import Subtopic, Discussion, Comments
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

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ('id', 'title', 'description', 'subtopic')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'text', 'owner', 'created_at', 'discussion_id')
