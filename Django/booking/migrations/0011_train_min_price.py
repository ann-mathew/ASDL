# Generated by Django 3.1.3 on 2021-01-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20210112_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='min_price',
            field=models.FloatField(default=200),
        ),
    ]
