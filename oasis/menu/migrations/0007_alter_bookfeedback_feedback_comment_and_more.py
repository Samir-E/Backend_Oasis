# Generated by Django 4.2.1 on 2023-06-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_bookfeedback_infoorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfeedback',
            name='feedback_comment',
            field=models.TextField(max_length=255, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_comment',
            field=models.TextField(max_length=255, verbose_name='Комментарий'),
        ),
    ]
