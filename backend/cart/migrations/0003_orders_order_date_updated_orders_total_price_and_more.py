# Generated by Django 4.2.1 on 2023-06-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_infoorder_servings_alter_orders_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления'),
        ),
        migrations.AddField(
            model_name='orders',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='infoorder',
            name='servings',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]
