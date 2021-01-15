from .models import Ticket, Train, Station, LockedSeat, TICKETS_NUMBER
from users.models import User, Passenger
from django.utils import timezone
import math
from users.selectors import getUserIDFromToken
from random import randrange

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

def seat_select():
    index = randrange(len(TICKETS_NUMBER) - 1)
    return TICKETS_NUMBER[index][0]

def mint_ticket(trainObj, userObj, boardingStation, destinationStation, dist, current_time, passenger, price, transactionId):
    passengerObj = Passenger.objects.create(**passenger)
    ticketObj = Ticket.objects.create(ticket_number=unique_key_generator(6), user=userObj, passenger=passengerObj, train=trainObj, seat_no=seat_select(), 
        book_date=current_time, price=price, boarding=boardingStation, destination=destinationStation, transaction_id=transactionId)
    return ticketObj.ticket_number


def book_tickets(train_id, token, boarding, destination, passenger_list):     # Work in Progress Function.
    user_id = getUserIDFromToken(token)
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
    price = (trainObj.total_seats - trainObj.remaining_seats)*1.5 + ( trainObj.min_price + dist )
    transaction_id = unique_key_generator(10)
    if trainObj.remaining_seats < 0:
        raise Exception("No seats left in this train.")

    for passenger in passenger_list:
        ticket_list.append(mint_ticket(trainObj, userObj, boardingStation, destinationStation, dist, current_time, passenger, price, transaction_id))
    return {"ticket_list": ticket_list, "price": price*len(passenger_list), "transaction_id": transaction_id}


def lock_seats(train_id, token, seats):

    user_id = getUserIDFromToken(token)
    trainObj = Train.objects.get(train_id = train_id)
    userObj = User.objects.get(pk = user_id)
    if trainObj.remaining_seats - seats >= 0:
        trainObj.remaining_seats = trainObj.remaining_seats - seats
        trainObj.save()
        lock = LockedSeat.objects.create(train_id=train_id, user_id=user_id, seats=seats, time=timezone.now())
        return seats
    else:
        return None


def cancel_ticket(ticket_number, token):
    user_id = getUserIDFromToken(token)
    ticket = Ticket.objects.get(ticket_number=ticket_number)

    if ticket.user.pk == user_id:
        ticket.delete()
    else:
        print(ticket.user.pk + "Not authorised to delete")     


def cancel_ticket_by_transaction(transaction_id, token):
    user_id = getUserIDFromToken(token)
    delete_list = []
    ticket_list = Ticket.objects.filter(transaction_id=transaction_id)
    for ticket in ticket_list:
        if ticket.user.pk == user_id:
            delete_list.append(ticket.ticket_number + " Cancelled")
            ticket.delete()
        else:
            delete_list.append(user_id + " not Authorised to cancel " + ticket.ticket_number + " which is owned by " + (ticket.user.full_name or ticket.user.username))
    
    return delete_list