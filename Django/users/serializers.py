from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'], validated_data['email'], validated_data['full_name'])
        #user['email'] = validated_data['email']
        #user['full_name'] = validated_data['full_name']
        return user

    class Meta:
        model = User 
        fields = [              
            "username",
            "password",
            "full_name",
            "email"
        ]
       
        
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(allow_blank=False)