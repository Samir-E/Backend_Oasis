from django.contrib.auth.models import User
from django.db import models
from django.db.models import ManyToManyField

from menu.models import Positions


# Create your models here.


class Orders(models.Model):
    """История заказов"""
    cart_num = models.OneToOneField('Cart', to_delete=models.PROTECT)
    item = models.ManyToManyField('OrderItem', to_delete=models.PROTECT)
    order_num = models.CharField(max_length=30,
                                 null=True,
                                 blank=True,
                                 unique=True,
                                 verbose_name='Порядковый номер')
    total_price = models.DecimalField('Сумма заказа',
                                      default=0.00,
                                      max_digits=10,
                                      decimal_places=2)
    create_order = models.DateTimeField('Дата и время заказа',
                                        auto_now_add=True)
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.PROTECT)

    # pay_status =
    # pay_number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_num


class OrderItem(models.Model):
    """Информация заказа"""

    # order = models.ForeignKey('Orders',
    #                           name='Заказ',
    #                           on_delete=models.PROTECT,
    #                           related_name='positions')
    positions = models.ForeignKey('menu.Positions', name='Позиция',
                                  on_delete=models.PROTECT)
    servings = models.PositiveIntegerField('Количество',
                                           default=1)
    total_price = models.DecimalField('Сумма',
                                      default=0.00,
                                      max_digits=7,
                                      decimal_places=2)

    class Meta:
        verbose_name = 'Информация о заказе'
        verbose_name_plural = verbose_name


#
#     def __str__(self):
#         return self.order.order_sn

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem', )
    date_created = models.DateTimeField(auto_now_add=True)

    # total_price = models.DecimalField(verbose_name='Сумма',
    #                                   default=0.00,
    #                                   max_digits=10,
    #                                   decimal_places=2)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name

    def search_item(self, position):
        for item in self.items.all():
            if item.position.id == int(position):
                return item
        return None

    """if user = request.user and  """

    def add_item(self, position=None, servings=None):
        if position is not None and servings is not None:
            position = Positions.objects.get(id=int(position))

            item = CartItem.objects.create(
                position=position,
                servings=servings,
            )

            self.items.add(item)
            return item
        return None

    def get_total(self):
        return sum(item.position.position_price * item.servings
                   for item in self.items.all())

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField('Количество', default=1)
    total_price = models.DecimalField(verbose_name='Сумма',
                                      blank=True,
                                      null=True,
                                      max_digits=10,
                                      decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.position.position_price * self.servings
        super().save(*args, **kwargs)

    # @classmethod
    # def create_cartitem1(cls, data):
    #     for item in data:
    #         cart_item1 = CartItem.objects.create(
    #             position=item['position'],
    #             servings=item['servings'],
    #         )

    def update_servings(self, servings):
        if int(servings) == 0:
            self.delete()
            return None
        else:
            self.servings = int(servings)
            return self.save()

    def __str__(self):
        return "Cart Item: " + str(self.position)
