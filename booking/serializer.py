from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import Gender

# <option value="Sleeper Class">Sleeper Class</option>
# <option value="Third AC">Third AC</option>
# <option value="Second AC">Second AC</option>
# <option value="First AC">First AC</option>
# <option value="Second Seating">Second Seating</option>
# <option value="AC Chair Car">AC Chair Car</option>
# <option value="First Class">First Class</option>
Class_Choices =  [
    ('Sleeper Class', 'Sleeper Class'),
    ('Third AC', 'Third AC'),
    ('First AC', 'First AC'),
    ('Second Seating', 'Second Seating'),
    ('AC Chair Car', 'AC Chair Car'),
    ('First Class', 'First Class'),
]

Berth_Choices = [
    ('Upper Berth', 'Upper Berth'),
    ('Middle Berth', 'Middle Berth'),
    ('Lower Berth', 'Lower Berth'),
    ('Side Lower', 'Side Lower'),
    ('Side Upper', 'Side Upper'),
]

class TrainQuerySerializer(serializers.Serializer):

    source = serializers.CharField(max_length=100, allow_blank=False)
    destination = serializers.CharField(max_length=100, allow_blank=False)
    time = serializers.DateField(format="%Y-%m-%d")
    coach_class = serializers.ChoiceField(choices=Class_Choices)
    seats = serializers.IntegerField()


class LockSeatsSerializer(serializers.Serializer):

    train_id = serializers.CharField(max_length=20, allow_blank=False)
    token = serializers.CharField(max_length=100, allow_blank=False)
    seats = serializers.IntegerField()

class PassengerDetailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100, allow_blank=False)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=Gender)
    berth = serializers.ChoiceField(choices=Berth_Choices)

class BookTicketSerializer(serializers.Serializer):

    train_id = serializers.CharField(max_length=20, allow_blank=False)
    token = serializers.CharField(max_length=100, allow_blank=False)
    boarding = serializers.CharField(max_length=20, allow_blank=False)
    destination = serializers.CharField(max_length=20, allow_blank=False)
    passenger_list = PassengerDetailSerializer(many=True)


class CancelTicketSerializer(serializers.Serializer):

    ticket_number = serializers.CharField(max_length=20, allow_blank=False)
    token = serializers.CharField(max_length=100, allow_blank=False)

class TransactionIDSerializer(serializers.Serializer):

    transaction_id = serializers.CharField(max_length=20, allow_blank=False)
    token = serializers.CharField(max_length=100, allow_blank=False)