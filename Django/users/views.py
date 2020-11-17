from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])  
def user_register(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data
            user['password'] = make_password(user['password'])
            user = User.objects.create(username=user['username'], password=user['password'])
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key} , status=status.HTTP_200_OK)