from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer, UserIDSerializer
from rest_framework.generics import GenericAPIView
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .selectors import getBookings, getUserData

from reservation.utils import ApiErrorsMixin


class UserRegister(ApiErrorsMixin, GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.data
            user['password'] = make_password(user['password'])
            userobj = User.objects.create(**user)
            if userobj:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(ApiErrorsMixin, GenericAPIView):
    serializer_class = LoginSerializer


    def post(self, request):
        cred = self.serializer_class(data=request.data)
        if not cred.is_valid():
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=cred.data["email"], password=cred.data["password"])
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_data': getUserData(user.pk)} , status=status.HTTP_200_OK)


class GetUserData(ApiErrorsMixin, GenericAPIView):

    serializer_class = UserIDSerializer
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = getUserData(**serializer.data)
            if user:
                print(json)
                return Response(user, status=status.HTTP_200_OK)
            else:
                return Response({"NONE":"USER_DOES_NOT_EXIST"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetBookings(ApiErrorsMixin, GenericAPIView):

    serializer_class = UserIDSerializer
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            bookings = getBookings(**serializer.data)
            if bookings:
                json = bookings
                print(json)
                return Response(json, status=status.HTTP_200_OK)
            else:
                return Response({"NONE":"No_BOOKINGS"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)