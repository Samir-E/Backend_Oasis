from rest_framework import serializers
from django.contrib.auth.models import User

from menu.serializers import PositionSerializer

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    order_num = serializers.CharField(read_only=True)

    """Функция создания номера заказа"""

    def generate_order_num(self):
        """идентификатор заказа + случайное число"""
        from random import Random
        random_ins = Random()
        order_num = "{orderid}" \
                    "{ranstr}".format(orderid=self.context['request'].order.id,
                                      ranstr=random_ins.randint(1, 99))
        return order_num

    class Meta:
        model = Orders
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    positions = PositionSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class AddItemToCartSerializer(serializers.Serializer):
    """Сериализатор для добавления товара в корзину"""
    position = serializers.CharField()
    servings = serializers.IntegerField(default=1)


class RemoveItemFromCartSerializer(serializers.Serializer):
    """Сериализатор для удаления товара из корзины"""
    position = serializers.CharField()


class CartItemSerializer(serializers.ModelSerializer):
    """"Сериализатор объектов товаров в корзине"""

    position = PositionSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"


class ListRetrieveUserSerializer(serializers.ModelSerializer):
    """Сериализатор для объекта пользователь"""

    class Meta:
        model = User
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    """Сериализатор объектов корзины"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    user = ListRetrieveUserSerializer()
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"
