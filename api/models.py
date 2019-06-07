from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.db                  import models
from django.conf                import settings
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, first_name=None, last_name=None, premium=False):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            premium=premium,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    uuid = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()), unique=True)
    username = models.CharField(max_length=16, null=False, unique=True, default='')
    email = models.EmailField(verbose_name='email address', max_length=255, null=False, unique=True)
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = UserManager()


class Subtopic(models.Model):
    uuid       = models.CharField(max_length=60, null=False, default=str(uuid.uuid4()))
    name       = models.CharField(max_length=20)
    private    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subtopic', on_delete=models.CASCADE)

class Discussion(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    upvote      = models.IntegerField(default=0)
    downvote    = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    owner       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
