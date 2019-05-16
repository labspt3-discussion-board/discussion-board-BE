from django.db import models

# Models
class User(models.Model):
    email      = models.CharField(max_length=20)
    username   = models.CharField(max_length=20)
    password   = models.CharField(max_length=20)
    premium    = models.BooleanField()
    created_at = models.DateTimeField()

class Subtopic(models.Model):
    name       = models.CharField(max_length=20)
    access     = models.BooleanField()
    created_at = models.DateTimeField()
    owner_id   = models.IntegerField()

class Discussion(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_at  = models.DateTimeField()
    owner_id    = models.IntegerField()
    subtopic_id = models.IntegerField()

class Comments(models.Model):
    text          = models.TextField(max_length=200)
    created_at    = models.DateTimeField()
    owner_id      = models.IntegerField()
    discussion_id = models.IntegerField()

# Relationships
class UserToSubtopic(models.Model):
    user_id     = models.IntegerField()
    subtopic_id = models.IntegerField()
