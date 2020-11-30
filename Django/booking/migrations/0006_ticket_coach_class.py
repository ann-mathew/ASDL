# Generated by Django 3.1.3 on 2020-11-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='coach_class',
            field=models.CharField(choices=[('Sleeper Class', 'Sleeper Class'), ('Third AC', 'Third AC'), ('First AC', 'First AC'), ('Second Seating', 'Second Seating'), ('AC Chair Car', 'AC Chair Car'), ('First Class', 'First Class')], default='Sleeper Class', max_length=15),
        ),
    ]
