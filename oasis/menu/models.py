from django.db import models

# Create your models here.
"""Категории товаров"""
class Sections(models.Model):
    section_name = models.CharField('Название категории', max_length=20)

    class Meta:
        
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

"""Товары из меню ресторана"""
class Positions(models.Model): 
    position_name = models.CharField('Название позиции', max_length=30)
    position_price = models.FloatField('Цена позиции', default=0.0)
    section = models.ForeignKey('Sections', name='Категория', 
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции' 

"""История заказов"""
class Orders(models.Model):
    ADOPTED = 'Принят'
    PREPARING = 'Готовится'
    CANCELLED = 'Отменен'
    READY = 'Готов'

    ORDER_STATUS_CHOISE = [
        (ADOPTED, 'Принят'),
        (PREPARING, 'Готовится'),
        (CANCELLED, 'Отменен'),
        (READY, 'Готов'),
    ]
    order_num = models.CharField('Номер заказа', max_length=6)
    order_date = models.DateTimeField('Дата и время заказа', auto_now=True)
    order_status = models.CharField('Статус заказа', max_length=9, 
                                    choices=ORDER_STATUS_CHOISE, 
                                    default=ADOPTED)
    paid_status = models.BooleanField

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 

"""Подробная инофрмация о заказах"""        
class InfoOrder (models.Model): #!!
    position = models.ForeignKey('Positions', name='Позиция', 
                                 on_delete=models.PROTECT)
    order = models.ForeignKey('Orders', name='Заказ', on_delete=models.CASCADE)
    servings = models.IntegerField
    order_price = models.FloatField

    class Meta:
        verbose_name = 'Информация о заказе'
        verbose_name_plural = 'Информация о заказах' 

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

"""Книга отзывов"""
class BookFeedback(models.Model):  
    fio = models.CharField('ФИО', max_length=40)
    email = models.EmailField('Электронная почта', max_length=30)
    feedback_comment = models.TextField('Комментарий', max_length=255)
    date_record = models.DateTimeField('Дата и время отзыва', 
                                       auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы' 