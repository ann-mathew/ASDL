# Generated by Django 3.1.3 on 2021-01-12 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20210112_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='arrival_time',
            new_name='start_time',
        ),
    ]
