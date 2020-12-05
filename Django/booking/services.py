from .models import Ticket, Train, Station
from Users.models import User
import time
import math


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def book_tickets(train_id, user_id, boarding, destination):
    trainObj = Train.objects.get(train_id = train_id)
    userObj = User.objects.get(pk = user_id)
    
    boardingStation = Station.objects.get(station_name = boarding)
    destinationStation = Station.objects.get(station_name = destination)
    dist = distance(boardingStation.coor(), destinationStation.coor)

    current_time = time.now()
    if trainObj.seats_left > 0:
        price = (dist+1) + (trainObj.total_seats - trainObj.seats_left) * 200 
    else:
        price = (dist+1) + (trainObj.total_seats - trainObj.seats_left) * 200 