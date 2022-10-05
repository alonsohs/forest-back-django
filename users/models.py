from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, default="")
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=15, default="")
    role = models.CharField(max_length=255, default="USER")
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, default="")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name', 'phone', 'date_of_birth']


