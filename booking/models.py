from django.db import models
from django.db.models.base import Model
from users.models import User, Passenger
import secrets

def get_code():
  return secrets.token_hex(4).upper()

# Create your models here.


class Station(models.Model):

    station_id = models.CharField(primary_key = True, max_length=10)
    station_name = models.CharField(max_length=100, default="ernakulam")
    station_address = models.CharField(max_length=100)

    def __str__(self):
        return self.station_name

class Route(models.Model):
    route_id = models.CharField(primary_key = True, max_length=10)
    train_id = models.CharField(default=None, max_length=10)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_index = models.PositiveIntegerField(default=1)
    expected_time = models.DateTimeField(default=None, blank=True)
    actual_time = models.DateTimeField(default=None, blank=True)
    def __str__(self):
            return self.train_id + " - " + self.station.station_id + " (" + str(self.route_index) + ")"

class Train(models.Model):

    train_id = models.CharField(primary_key = True, max_length=10)
    train_name = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    remaining_seats = models.IntegerField(default=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    min_price = models.FloatField(default=200)
    route_table = models.ManyToManyField(Route, blank=True)
    route = models.ManyToManyField(Station)
    def __str__(self):
        return self.train_name





TICKETS_NUMBER = [('A1', 'A1'),]
for pre in range(ord('A'), ord('Z')+1):
    for fix in range(100):
        val = str(chr(pre)+ "-" + str(fix))
        TICKETS_NUMBER.append((val, val))
TICKETS_NUMBER = tuple(TICKETS_NUMBER)

class Ticket(models.Model):

    ticket_id = models.CharField(primary_key = True, max_length=10, default=get_code, editable=False)
    ticket_number = models.CharField(max_length=10, default = 10)
    user = models.ForeignKey(User, null=True,  on_delete=models.SET_NULL)
    passenger = models.ForeignKey(Passenger, null=True,  on_delete=models.SET_NULL)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=5, choices=TICKETS_NUMBER)
    book_date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_id = models.CharField(max_length=10, default = 10)
    boarding = models.ForeignKey(Station, related_name='boarding',  on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, related_name='destination', on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket_number

class LockedSeat(models.Model):

    user = models.ForeignKey(User, null=True,  on_delete=models.SET_NULL)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seats = models.IntegerField()
    time = models.DateTimeField(null=True)
