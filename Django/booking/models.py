from django.db import models
from django.db.models.base import Model
from users.models import User
# Create your models here.


class Station(models.Model):

    station_id = models.CharField(primary_key = True, max_length=10)
    station_name = models.CharField(max_length=100)
    station_address = models.CharField(max_length=100)

    def __str__(self):
        return self.station_name


class Train(models.Model):

    train_id = models.CharField(primary_key = True, max_length=10)
    train_name = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    route = models.ManyToManyField(Station)



    def __str__(self):
        return self.train_name



TICKETS_NUMBER = [('A1', 'A1'),]
for pre in range(ord('A'), ord('Z')+1):
    for fix in range(100):
        val = str(chr(pre)+ "-" + str(fix))
        TICKETS_NUMBER.append((val, val))
TICKETS_NUMBER = tuple(TICKETS_NUMBER)

COACH_CLASS = Class_Choices =  [
    ('Sleeper Class', 'Sleeper Class'),
    ('Third AC', 'Third AC'),
    ('First AC', 'First AC'),
    ('Second Seating', 'Second Seating'),
    ('AC Chair Car', 'AC Chair Car'),
    ('First Class', 'First Class'),
]


class Ticket(models.Model):

    ticket_id = models.CharField(primary_key = True, max_length=10)
    ticket_number = models.CharField(max_length=10) 
    user = models.ForeignKey(User, null=True,  on_delete=models.SET_NULL)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=5, choices=TICKETS_NUMBER)
    book_date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    coach_class = models.CharField(max_length=15, choices=COACH_CLASS, default ='Sleeper Class')
    boarding = models.ForeignKey(Station, related_name='boarding',  on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, related_name='destination', on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket_number







