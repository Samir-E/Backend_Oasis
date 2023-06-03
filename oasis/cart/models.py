from django.db import models

# Create your models here.
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
    order_status = models.CharField('Статус заказа', max_length=9,  #!!
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
    servings = models.IntegerField('Количество', default=0)
    order_price = models.FloatField('Сумма', default=0)

    class Meta:
        verbose_name = 'Информация о заказе'
        verbose_name_plural = 'Информация о заказах' 