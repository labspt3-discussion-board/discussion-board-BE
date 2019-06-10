from rest_framework             import serializers
# from django.contrib.auth.models import User
from api.models                 import Subtopic, Discussion, Comments
from django.conf                import settings
from django.contrib.auth        import get_user_model
from django.db.models           import Count


class SubtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = ('id', 'name', 'private', 'created_at', 'owner')

class UserSerializer(serializers.ModelSerializer):
    subtopics = SubtopicSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'premium', 'created_at', 'auth_type', 'subtopics')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'text', 'owner', 'created_at', 'discussion_id')


class DiscussionSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=[])
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'title', 'description', 'upvote', 'downvote', 'owner', 'created_at', 'subtopic', 'comments', 'comment_count')
