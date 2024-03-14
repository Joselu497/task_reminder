from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    pass

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True ,max_length=64)
    email = models.CharField(unique=True)
    password = models.CharField()
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']