from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from reservation.utils import ApiErrorsMixin, get_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import getAvailableTrains, getTicketDetails, getTrainDetails, getTransactionDetails
from .serializer import (BookTicketSerializer, LockSeatsSerializer,
                         PassengerDetailSerializer, TrainQuerySerializer, CancelTicketSerializer, TransactionIDSerializer)
from .services import (book_tickets, lock_seats, cancel_ticket, cancel_ticket_by_transaction)


class GetAvailableTrains(ApiErrorsMixin, GenericAPIView):

    serializer_class = TrainQuerySerializer

    @swagger_auto_schema(operation_description="Get All the available trains. \n\n Returns Two keys: avail_trains and \ reserved_trains.",
                         responses={ 200: 'Trains Retrieved',
                                404: 'If no trains available',
                                400: 'If Invalid POST Body Format'})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            avail_trains = getAvailableTrains(**serializer.data)
            if avail_trains:
                json = avail_trains
                return Response(json, status=status.HTTP_200_OK)
            else:
                return Response({"NONE":"No_TRAINS_AVAILABLE"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LockSeatsView(ApiErrorsMixin, GenericAPIView):

    serializer_class = LockSeatsSerializer

    @swagger_auto_schema(operation_description="Freeze n number of seats in the train. \n Call this API before booking screen in your app. \
            \n Only frozen for 15 minutes \n\n Returns number of seats frozen.",
                         responses={ 201: 'Seats Locked Successfully',
                                404: 'If No Seats left.',
                                400: 'If Invalid POST Body Format'})
    def post(self, request):
        token = get_token(request)
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        seats = lock_seats(**serializer.data)
        
        if seats:
            return Response({"Success": "Locked " + str(seats) + " Seats for 15 minutes."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERROR":"NOT_ENOUGH_SEATS_AVAILABLE"}, status=status.HTTP_404_NOT_FOUND)
      
class BookTicketView(ApiErrorsMixin, GenericAPIView):

    serializer_class = BookTicketSerializer
    @swagger_auto_schema(operation_description="API to book tickets.",
                        responses={ 201: 'Tickets Booked Successfully.\n\n Returns list of ticket numbers.',
                            409: 'If tickets full or some conflict in database.',
                            404: 'If ticket already exists?',
                            400: 'If Invalid POST Body Format'})
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

      
class GetTicketView(ApiErrorsMixin, GenericAPIView):
    
    @swagger_auto_schema(operation_description="API to Get Specific ticket details from ticket number.",
                        responses={ 200: 'Ticket Details Retrieved. \n\n Returns details of ticket.',
                            404: 'If ticket does not exists',})
    def get(self, request, ticket_id):
        try:
            ticket = getTicketDetails(ticket_id)
            return Response(ticket, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_404_NOT_FOUND)

class GetTrainView(ApiErrorsMixin, GenericAPIView):
    @swagger_auto_schema(operation_description="API to Get Specific train details from train number.",
                        responses={ 200: 'Train Details Retrieved. \n\n Returns details of train.',
                            404: 'If train does not exists',})
    def get(self, request, train_id):
        try:
            train = getTrainDetails(train_id)
            return Response(train, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_404_NOT_FOUND)


class CancelSingleTicketView(ApiErrorsMixin, GenericAPIView):
    
    serializer_class = CancelTicketSerializer
    @swagger_auto_schema(operation_description="API to Cancel Specific ticket details from ticket number.",
                        responses={ 200: 'Ticket Details Retrieved. \n\n Returns details of ticket.',
                            404: 'If ticket does not exists',
                            409: 'Invalid Token',
                            400: 'Bad POST Body'})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                train = cancel_ticket(**serializer.validated_data)
                return Response({"SUCCESS": "TICKET_CANCELLED"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_409_CONFLICT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CancelTicketByTransactionView(ApiErrorsMixin, GenericAPIView):
    
    serializer_class = TransactionIDSerializer
    @swagger_auto_schema(operation_description="API to Cancel all tickets of a transaction_id.",
                        responses={ 200: 'Ticket Details Retrieved. \n\n Returns details of ticket.',
                            404: 'If transaction does not exists',
                            409: 'Invalid Token',
                            400: 'Bad POST Body'})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                tickets = cancel_ticket_by_transaction(**serializer.validated_data)
                if tickets:
                    return Response({"SUCCESS": "TICKETS_CANCELLED", 'data':tickets}, status=status.HTTP_200_OK)
                else:
                    return Response({"ERROR": "TRANSACTION_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_409_CONFLICT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailsView(ApiErrorsMixin, GenericAPIView):
    
    serializer_class = TransactionIDSerializer
    @swagger_auto_schema(operation_description="API to Get all ticket of a particular transaction.",
                        responses={ 200: 'Ticket Details Retrieved. \n\n Returns details of ticket.',
                            404: 'If ticket does not exists',
                            409: 'Invalid Token',
                            400: 'Bad POST Body'})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                tickets = getTransactionDetails(**serializer.validated_data)
                return Response({"transaction_tickets": tickets}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'ERROR': type(e).__name__, "MESSAGE": str(e)}, status=status.HTTP_409_CONFLICT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)