from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    phoneNo = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)


    class Meta:
        ordering=["-timestamp", "-updated"]