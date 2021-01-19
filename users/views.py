from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from reservation.utils import ApiErrorsMixin
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User

from .selectors import getBookings, getUserData
from .serializers import (LoginSerializer, SetUserDataSerializer,
                          TokenSerializer, UserIDSerializer, UserSerializer)
from .services import deleteUser, setUserData


##############################################################################################################################
class UserRegister(ApiErrorsMixin, GenericAPIView):
    serializer_class = UserSerializer
    @swagger_auto_schema(operation_description="API to Register New Accounts \n Returns Success message.",
                        responses={ 201: 'Registered User.',
                            409: 'If User with given values already exists. Returns the values that is conflicting as list.',
                            400: 'Invalid POST body format.'})
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.data
            user['password'] = make_password(user['password'])
            userobj = User.objects.create(**user)
            if userobj:
                return Response({"SUCCCESS": "USER_CREATED_SUCCESSFULLY"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#######################################################

class UserLogin(ApiErrorsMixin, GenericAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(operation_description="API to Login\n Returns Token and user details.",
                        responses={ 200: 'Logged in User.',
                            409: 'If Invalid Credentials',
                            400: 'Invalid POST body format.'})
    def post(self, request):
        cred = self.serializer_class(data=request.data)
        if not cred.is_valid():
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=cred.data["email"], password=cred.data["password"])
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_409_CONFLICT)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_data': getUserData(token)} , status=status.HTTP_200_OK)

##############################################################################################################

class GetUserData(ApiErrorsMixin, GenericAPIView):

    serializer_class = TokenSerializer

    @swagger_auto_schema(operation_description="API to get user data \n Returns user data",
                        responses={ 201: 'User Data Got.',
                            404: 'If User Does not exist',
                            400: 'Invalid POST body format.'})
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = getUserData(**serializer.data)
            if user:
                return Response(user, status=status.HTTP_200_OK)
            else:
                return Response({"NONE":"USER_DOES_NOT_EXIST"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#######################################################

class SetUserDataView(ApiErrorsMixin, GenericAPIView):
    serializer_class = SetUserDataSerializer

    @swagger_auto_schema(operation_description="API to Edit Some User Data.\n \
        Only need to send keys that need to be edited (i.e none of the keys are really required)",
                        responses={ 200: 'Data set for User.',
                            409: 'User info conflicts with other users.',
                            400: 'Invalid POST body format.'})
    def put(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if not serializer_data.is_valid():
            return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = setUserData(serializer_data.validated_data)
            return Response({"SUCCESS": "USER_DATA_SET:"+str(user)} , status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_409_CONFLICT)

#######################################################

class DeleteUserView(ApiErrorsMixin, GenericAPIView):
    serializer_class = TokenSerializer

    @swagger_auto_schema(operation_description="API to Delete User Account.",
                        responses={ 200: 'User Deleted Successfully.',
                            409: '?',
                            400: 'Invalid POST body format.'})
    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if not serializer_data.is_valid():
            return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = deleteUser(**serializer_data.validated_data)
            return Response({"SUCCESS": "USER_DELETED"} , status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_409_CONFLICT)
        

##############################################################################################################

class GetBookings(ApiErrorsMixin, GenericAPIView):

    serializer_class = TokenSerializer


    @swagger_auto_schema(operation_description="API to Get all bookings, grouped by transactions id\n Returns: https://pastebin.com/EX0nQByB ",
                        responses={ 200: 'If Success',
                            404: 'If No Bookings',
                            400: 'Invalid POST body format.'})
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            bookings = getBookings(**serializer.validated_data)
            if bookings:
                return Response(bookings, status=status.HTTP_200_OK)
            else:
                return Response({"NONE":"No_BOOKINGS"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
