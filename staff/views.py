from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


from reservation.utils import ApiErrorsMixin


class CreateTrain(ApiErrorsMixin, GenericAPIView):
    serializer_class = 

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():


            if True:
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)