from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


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

Sex_Choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender'),
]

Berth_Choices = [
    ('Upper Berth', 'Upper Berth'),
    ('Middle Berth', 'Middle Berth'),
    ('Lower Berth', 'Lower Berth'),
]

class TrainQuerySerializer(serializers.Serializer):

    source = serializers.CharField(max_length=100, allow_blank=False)
    destination = serializers.CharField(max_length=100, allow_blank=False)
    time = serializers.DateField(format="%Y-%m-%d")
    coach_class = serializers.ChoiceField(choices=Class_Choices)
    seats = serializers.IntegerField()


class LockSeatsSerializer(serializers.Serializer):

    train_id = serializers.CharField(max_length=20, allow_blank=False)
    user_id = serializers.CharField(max_length=20, allow_blank=False)
    seats = serializers.IntegerField()

class PassengerDetailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=20, allow_blank=False)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=Sex_Choices)
    berth = serializers.ChoiceField(choices=Berth_Choices)

class BookTicketSerializer(serializers.Serializer):

    train_id = serializers.CharField(max_length=20, allow_blank=False)
    user_id = serializers.CharField(max_length=20, allow_blank=False)
    boarding = serializers.CharField(max_length=20, allow_blank=False)
    destination = serializers.CharField(max_length=20, allow_blank=False)
    passenger_list = PassengerDetailSerializer(many=True)
