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

class TrainQuerySerializer(serializers.Serializer):

    source = serializers.CharField(max_length=100, allow_blank=False)
    destination = serializers.CharField(max_length=100, allow_blank=False)
    time = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    coach_class = serializers.ChoiceField(choices=Class_Choices)
    seats = serializers.IntegerField()

