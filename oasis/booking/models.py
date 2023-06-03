from django.db import models

# Create your models here.
"""Бронирование столиков""" 
class Booking(models.Model): 
    ADOPTED = 'Принят'
    CONFIRMED = 'Подтвержден'
    CANCELLED = 'Отменен'
    COMPLITED = 'Выполнен'

    BOOKING_STATUS_CHOISE = [
        (ADOPTED, 'Принят'),
        (CONFIRMED, 'Подтвержден'),
        (CANCELLED, 'Отменен'),
        (COMPLITED, 'Выполнен'),
    ]

    fio = models.CharField('ФИО', max_length=40)
    mobile_number = models.CharField('Номер телефона', max_length=11)
    booking_status = models.CharField('Статус брони', max_length=11, 
                                      choices=BOOKING_STATUS_CHOISE, 
                                      default=ADOPTED)
    booking_comment = models.TextField('Комментарий', max_length=255) 
    date_reg = models.DateTimeField('Дата и время регистрации брони', 
                                    auto_now=True)
    date_booking = models.DateTimeField('Дата и время брони')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони' 