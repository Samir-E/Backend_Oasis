# Generated by Django 4.2.1 on 2023-06-12 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_total_price_cartitem_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='total_price',
        ),
    ]
