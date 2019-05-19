from django.db import models
import uuid

# Models
class User(models.Model):
    uuid       = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()))
    username   = models.CharField(max_length=20, null=True)
    email      = models.CharField(max_length=20, null=True)
    password   = models.CharField(max_length=20, null=True)
    premium    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Subtopic(models.Model):
    name       = models.CharField(max_length=20)
    access     = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner_id   = models.IntegerField()

class Discussion(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    owner_id    = models.IntegerField()
    subtopic_id = models.IntegerField()

class Comments(models.Model):
    text          = models.TextField(max_length=200)
    created_at    = models.DateTimeField(auto_now_add=True)
    owner_id      = models.IntegerField()
    discussion_id = models.IntegerField()

# Relationships
class UserToSubtopic(models.Model):
    user_id     = models.IntegerField()
    subtopic_id = models.IntegerField()
