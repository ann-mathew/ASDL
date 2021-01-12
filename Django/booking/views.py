from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from reservation.utils import ApiErrorsMixin, get_token
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .serializer import TrainQuerySerializer, LockSeatsSerializer, PassengerDetailSerializer, BookTicketSerializer
from .selectors import getAvailableTrains, getTicketDetails, getTrainDetails
from .services import book_tickets, lock_seats

class GetAvailableTrains(ApiErrorsMixin, GenericAPIView):

    serializer_class = TrainQuerySerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            avail_trains = getAvailableTrains(**serializer.data)
            if avail_trains:
                json = avail_trains
                return Response(json, status=status.HTTP_201_CREATED)
            else:
                return Response({"NONE":"No_TRAINS_AVAILABLE"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LockSeatsView(ApiErrorsMixin, GenericAPIView):

    serializer_class = LockSeatsSerializer
    def post(self, request):
        token = get_token(request)
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        seats = lock_seats(**serializer.data)
        
        if seats:
            return Response({"Success": "Locked " + str(seats) + " Seats"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"NONE":"No_TRAINS_AVAILABLE"}, status=status.HTTP_404_NOT_FOUND)
      
class BookTicketView(ApiErrorsMixin, GenericAPIView):

    serializer_class = BookTicketSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                passenger = book_tickets(**serializer.data)
                if passenger:
                    json = passenger
                    return Response(json, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error":"ticket already exists"}, status=status.HTTP_404_NOT_FOUND)   
            except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_409_CONFLICT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class GetTicketView(ApiErrorsMixin, APIView):

    def get(self, request, ticket_id):
        try:
            ticket = getTicketDetails(ticket_id)
            return Response(ticket, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_404_NOT_FOUND)

class GetTrainView(ApiErrorsMixin, GenericAPIView):

    def get(self, request, train_id):
        try:
            train = getTrainDetails(train_id)
            return Response(train, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_404_NOT_FOUND)

