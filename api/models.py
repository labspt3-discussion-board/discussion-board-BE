from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.db                  import models
from django.conf                import settings
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name=None, last_name=None, premium=False, auth_type='api_model'):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            premium=premium,
            auth_type=auth_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    username     = models.CharField(max_length=16, null=False, unique=True, default='')
    email        = models.EmailField(verbose_name='email address', max_length=255, null=False, unique=True)
    first_name   = models.CharField(max_length=200, default='')
    last_name    = models.CharField(max_length=200, default='')
    premium      = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    auth_type    = models.CharField(max_length=255, null=False, unique=False, default='api_model')
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Subforum(models.Model):

    name       = models.CharField(max_length=20)
    private    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subforum', on_delete=models.CASCADE)

class Discussion(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    upvote      = models.IntegerField(default=0)
    downvote    = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    owner       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subforum    = models.ForeignKey(Subforum, on_delete=models.CASCADE)

class Comments(models.Model):
    text          = models.TextField(max_length=200)
    created_at    = models.DateTimeField(auto_now_add=True)
    owner         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    discussion_id = models.ForeignKey(Discussion, related_name='comments', on_delete=models.CASCADE)

# Relationships
class UserToSubforum(models.Model):
    user_uuid     = models.IntegerField()
    Subforum_uuid = models.IntegerField()
