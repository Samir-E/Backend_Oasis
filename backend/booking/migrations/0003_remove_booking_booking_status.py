# Generated by Django 4.2.1 on 2023-06-10 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_status',
        ),
    ]