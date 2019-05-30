from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db                  import models
from django.conf                import settings
import uuid

# Manager
# class UserManager(BaseUserManager):
#     def create_user(self, uuid, username, email, password):

#         if not uuid:
#             raise ValueError('uuid must be defined')

#         if not email:
#             raise ValueError('email must be defined')

#         if not password:
#             raise ValueError('password must be defined')

#         user = self.model(uuid=uuid, username=username, email=self.normalize_email())
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, uuid, username, email, password):

#         user = self.create_user(uuid, username, email, password)
#         user.is_admin = True
#         user.save(using=self.db)
#         return user


# Models
class User(AbstractUser): # Extend the default Django user model
    uuid            = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()), unique=True)
    username        = models.CharField(max_length=255, null=False, unique=True)
    email           = models.EmailField(verbose_name='email address', max_length=255, null=False, unique=True)
    password        = models.CharField(max_length=255, null=False)
    premium         = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)

    # objects = UserManager()

    UUID_FIELD      = 'identifier'
    REQUIRED_FIELDS = ['uuid', 'email']

    # def __str__(self):
        # return self.email

    # def has_perm(self, perm, obj=None):
        # return True

    # def has_module_perms(self, api):
        # return True



class Subtopic(models.Model):
    uuid       = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()))
    name       = models.CharField(max_length=20)
    private    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Discussion(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    upvote      = models.IntegerField(default=0)
    downvote    = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
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
