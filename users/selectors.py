from booking.models import Ticket
from .models import User
from datetime import datetime
import pytz
from django.utils import timezone
from rest_framework.authtoken.models import Token

def getBookings(token: str):
    user = getUserIDFromToken(token)
    unqiue_transactions = list(Ticket.objects.filter(user=user).values("transaction_id").distinct())
    bookings = {}

    for transact in unqiue_transactions:
        id = transact['transaction_id']
        ticket_list = Ticket.objects.filter(transaction_id = id)
        bookings[id] = []
        index = 1
        for ticket in ticket_list:
            data = {
                "ticket_number":ticket.ticket_number,
                "transaction_id": ticket.transaction_id,
                "passenger":{
                    "name":ticket.passenger.name,
                    "gender":ticket.passenger.gender,
                    "age":ticket.passenger.age,
                    "berth":ticket.passenger.berth,
                    },
                "train":{
                    "train_name":ticket.train.train_name,
                    "arrival_time":ticket.train.start_time,
                    "departure_time":ticket.train.end_time,
                },
                "seat_no":ticket.seat_no,
                "price":ticket.price,
                "boarding":ticket.boarding.station_name,
                "destination":ticket.destination.station_name
            }  
            bookings[id].append({"ticket_id": ticket.ticket_number, "data": data})
            index = index + 1
    # for ticket in allBookings:
    #     bookings[ticket.ticket_number] = {
    #     "ticket_number":ticket.ticket_number,
    #     "passenger":{
    #         "name":ticket.passenger.name,
    #         "gender":ticket.passenger.gender,
    #         "age":ticket.passenger.age,
    #         "berth":ticket.passenger.berth,
    #         },
    #     "train":{
    #         "train_name":ticket.train.train_name,
    #         "arrival_time":ticket.train.start_time,
    #         "departure_time":ticket.train.end_time,
    #     },
    #     "seat_no":ticket.seat_no,
    #     "price":ticket.price,
    #     "boarding":ticket.boarding.station_name,
    #     "destination":ticket.destination.station_name
    # }               
                      
    if not bool(bookings):
        return None
    else:
        return {'transactions_count': len(unqiue_transactions), 'bookings': bookings }


def getUserData(user: str):
    user = User.objects.get(pk=user)

    data = {
        "user_id": user.pk,
        "full_name": user.full_name,
        "phoneNo": user.phoneNo,
        "age": user.age,
        "email": user.email,
        "last_login": user.updated,
        "role": user.role,

    }
    return data

def getUserIDFromToken(token:str):
    token = Token.objects.get(pk=token)
    user = token.user
    return user.pk