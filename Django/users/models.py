from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets

def get_code():
  return secrets.token_hex(4).upper()


Roles = (("USER", "User"), ("ROC", "ROC"), ("ADMIN", "Admin"))

class User(AbstractUser):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default = "invalid@gmail.com", unique=True)
    phoneNo = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    role = models.CharField(max_length=20, choices = Roles, default="USER")

    def __str__(self):
            return self.full_name or self.email
    class Meta:
        ordering=["-timestamp", "-updated"]

Gender = (("Male", "M"), ("Female", "F"), ("Other", "Other"))

class Passenger(models.Model):
    passenger_id = models.CharField(max_length=32, primary_key=True, default=get_code, editable=False)
    name = models.CharField(max_length=100)
    gender = (models.CharField(max_length=20, choices = Gender))
    age = models.IntegerField(null=True)
    berth = models.CharField(max_length=20, default="Upper Berth")

    def __str__(self):
        return self.name