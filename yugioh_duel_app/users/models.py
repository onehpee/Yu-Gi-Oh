# models.py — defines your database structure
# Models define the data your application stores. Django uses them to create and interact with database tables.

from datetime import timezone

from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, first_name, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if not other_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not other_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(first_name, username, email, password, **other_fields)

    def create_user(self, username, email, first_name, password, **other_fields):
        #Validation
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not password:
            raise ValueError('Users must have a password')

        email = self.normalize_username(email)
        user = self.model(username=username, email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


# Creating a Custom User Model For New Users

class NewUser(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True,
                              error_messages={'unique': 'A user with that email already existss.'})
    password = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    # Allows this user to access the admin site.
    is_staff = models.BooleanField(default=False)
    # Marks user account as active
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    def __str__(self):
        return self.username
