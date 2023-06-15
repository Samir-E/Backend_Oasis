from django.db import models


# Create your models here.


class Sections(models.Model):
    """
    Категории товаров
    """
    section_name = models.CharField('Название категории', max_length=20)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.section_name


class Positions(models.Model):
    """
    Товары из меню ресторана
    """
    position_name = models.CharField('Название позиции', max_length=30)
    position_price = models.DecimalField('Цена позиции',
                                         default=0.0,
                                         max_digits=5,
                                         decimal_places=2)
    section = models.ForeignKey('Sections', verbose_name='Категория',
                                on_delete=models.PROTECT,
                                null=True)

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

    def __str__(self):
        return self.position_name
