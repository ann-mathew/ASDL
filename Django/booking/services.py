from .models import Ticket, Train, Station, LockedSeat
from users.models import User, Passenger
from django.utils import timezone
import math


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def unique_key_generator(key_len):
    # By Sandeep Pillai
    if key_len > 10:
        raise ValueError("Cannot Generate a key over length 10")

    now = timezone.now() # current date and time
    time_string = now.strftime("%H%M%S%f%Y%m%d")
    time_string = time_string[0:(key_len*2)]
    key_string = ""
    for index in range(0, len(time_string), 2):
        val = time_string[index:index+2]
        key_string += chr(65 + int(val)%26)


    return str(key_string)

def mint_ticket(trainObj, userObj, boardingStation, destinationStation, dist, current_time, passenger, price):
    passengerObj = Passenger.objects.create(**passenger)
    ticketObj = Ticket.objects.create(ticket_number=unique_key_generator(6), user=userObj, passenger=passengerObj, train=trainObj, seat_no="A", 
        book_date=current_time, price=price, boarding=boardingStation, destination=destinationStation)
    return ticketObj.pk


def book_tickets(train_id, user_id, boarding, destination, passenger_list):     # Work in Progress Function.
    ticket_list =[]
    trainObj = Train.objects.get(train_id = train_id)
    userObj = User.objects.get(pk = user_id)
    print("1")
    boardingStation = Station.objects.get(station_name = boarding)
    destinationStation = Station.objects.get(station_name = destination)
    #dist = distance(boardingStation.coor(), destinationStation.coor())
    dist = 100
    print("2")
    current_time = timezone.now()
    if trainObj.remaining_seats > 0:
        price = (dist+1) + (trainObj.total_seats - trainObj.remaining_seats) * 200 
    else:
        price = (dist+1) + (trainObj.total_seats - trainObj.remaining_seats) * 200 
    for passenger in passenger_list:
        ticket_list.append(mint_ticket(trainObj, userObj, boardingStation, destinationStation, dist, current_time, passenger, price))
    return ticket_list


def lock_seats(train_id, user_id, seats):

    trainObj = Train.objects.get(train_id = train_id)
    userObj = User.objects.get(pk = user_id)
    trainObj['remaining_seats'] = trainObj['remaining_seats'] - seats

    lock = LockedSeat.objects.create(train_id, user_id, seats)

    

