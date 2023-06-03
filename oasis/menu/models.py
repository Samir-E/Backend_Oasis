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
