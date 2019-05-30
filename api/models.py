from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db                  import models
from django.conf                import settings
import uuid


"""

# Models
class User(AbstractUser): # Extend the default Django user model
    uuid            = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()), unique=True)
    # username        = models.CharField(max_length=20, null=False, unique=True)
    # email           = models.EmailField(verbose_name='email address', max_length=255, null=False, unique=True)
    # password        = models.CharField(max_length=20, null=False)
    premium         = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)

    UUID_FIELD      = 'identifier'
    REQUIRED_FIELDS = ['uuid', 'email']

    # def __str__(self):
        # return self.email

    # def has_perm(self, perm, obj=None):
        # return True

    # def has_module_perms(self, api):
        # return True
"""


class Subtopic(models.Model):
    uuid       = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()))
    name       = models.CharField(max_length=20)
    private    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner      = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Discussion(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    owner       = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subtopic    = models.ForeignKey(Subtopic, on_delete=models.CASCADE)

class Comments(models.Model):
    text          = models.TextField(max_length=200)
    created_at    = models.DateTimeField(auto_now_add=True)
    owner         = models.IntegerField()
    discussion_id = models.IntegerField()

# Relationships
class UserToSubtopic(models.Model):
    user_uuid     = models.IntegerField()
    subtopic_uuid = models.IntegerField()
