# Generated by Django 3.1.2 on 2020-12-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20201205_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='remaining_seats',
            field=models.IntegerField(default=100),
        ),
    ]
