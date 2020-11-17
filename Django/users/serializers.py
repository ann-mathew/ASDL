from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user

    class Meta:
        model = User 
        fields = [              
            "username",
            "password",
        ]
       
        
