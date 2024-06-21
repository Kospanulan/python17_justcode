from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authorization.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    SUPERUSER, MODERATOR, USER = 1, 2, 3

    ROLES = (
        (SUPERUSER, 'Superuser'),
        (MODERATOR, 'Moderator'),
        (USER, 'User')
    )

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role = models.IntegerField(choices=ROLES, default=USER)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []






