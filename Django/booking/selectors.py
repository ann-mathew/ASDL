from .models import Ticket, Train, Station
from datetime import datetime
import pytz
from django.utils import timezone

def getAvailableTrains(source: str, destination: str, time, coach_class: str, seats: int):

    allTrains = Train.objects.all()

    time = datetime.strptime(time, "%Y-%m-%d")
    time = pytz.utc.localize(time)

    avail_train = {}
    reserved_train = {}

    for train in allTrains:
        if time<train.arrival_time: 
            if train.route.filter(station_name=source).first():
                if train.route.filter(station_name=destination).first():

                        if train.remaining_seats > seats:
        
                            avail_train[train.train_id] = {
                                        "train_id": train.train_id,
                                        "train_name": train.train_name,
                                        "available_seats": train.remaining_seats,
                                        "arrival": train.arrival_time,
                                        "departure": train.departure_time,
                                        
                            }
                        else:
                            reserved_train[train.train_id] = {
                                        "train_id": train.train_id,
                                        "train_name": train.train_name,
                                        "reservation_queue": -(train.remaining_seats - 1),
                                        "arrival": train.arrival_time,
                                        "departure": train.departure_time,
                                        
                            }

            

    if not bool(avail_train) and not bool(reserved_train):  
        return None
    else:
        return { 'avail_train': avail_train, 'reserved_train': reserved_train }

def getTicketDetails(ticket_id):
    ticket = Ticket.objects.get(ticket_number=ticket_id)
    data = {
        "ticket_number":ticket.ticket_number,
        "passenger":{
            "name":ticket.passenger.name,
            "gender":ticket.passenger.gender,
            "age":ticket.passenger.age,
            "berth":ticket.passenger.berth,
            },
        "train":{
            "train_name":ticket.train.train_name,
            "arrival_time":ticket.train.arrival_time,
            "departure_time":ticket.train.departure_time,
        },
        "seat_no":ticket.seat_no,
        "price":ticket.price,
        "boarding":ticket.boarding.station_name,
        "destination":ticket.destination.station_name
    }
    return data

def getTrainDetails(train_id):
    train = Train.objects.get(pk=train_id)
    data = {
            "train_id":train.train_id,
            "total_seats":train.total_seats,
            "remaining_seats":train.remaining_seats,
            "train_name":train.train_name,
            "arrival_time":train.arrival_time,
            "departure_time":train.departure_time,
        }
    return data