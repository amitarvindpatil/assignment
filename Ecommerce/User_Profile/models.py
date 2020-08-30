from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager For UserProfile"""
    def create_user(self,email,name,password=None,**extra_fields):
        """Create New User Prfile"""
        if not email:
            raise ValueError('User Must have an email address')

        email = self.normalize_email(email)
        user  = self.model(email=email,name=name,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password,**extra_fields):
        """create and save new superuser with given details"""
        user = self.create_user(email,name,password,**extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ DataBase model for user in a system  """
    email = models.EmailField(max_length=255,unique=True)
    name  = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    roles_data = [
            ('customer', 'customer'),
            ('vendor', 'vendor'),
    ]
    roles = models.CharField(max_length=50,choices=roles_data)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','roles']

    def __str__(self):
        return self.email
