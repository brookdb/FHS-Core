import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    token = models.CharField(max_length=44, blank=True)
    is_member = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        app_label = 'users'
        ordering = ['last_name']

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    avatar = models.ImageField(default='main/img/profile/default.png', blank=True, null=True, upload_to='main/img/profile/')
    bio = models.TextField(blank=True, null=True, verbose_name='Biogrophy')
    inspo = models.TextField(blank=True, null=True, verbose_name='Inspirations')
    location = models.CharField(blank=True, null=True, max_length=20, verbose_name='Location')
    is_paid_member=models.BooleanField(default=False)
    is_leadership = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ['user']
