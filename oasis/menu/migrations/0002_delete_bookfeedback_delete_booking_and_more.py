# Generated by Django 4.2.1 on 2023-05-31 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookFeedback',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.AlterModelOptions(
            name='infoorder',
            options={'verbose_name': 'Информация о заказе', 'verbose_name_plural': 'Информация о заказах'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='positions',
            options={'verbose_name': 'Позиция', 'verbose_name_plural': 'Позиции'},
        ),
        migrations.AlterModelOptions(
            name='sections',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='positions',
            old_name='section',
            new_name='Категория',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время заказа'),
        ),
        migrations.AddField(
            model_name='positions',
            name='position_price',
            field=models.FloatField(default=0.0, verbose_name='Цена позиции'),
        ),
        migrations.AlterField(
            model_name='infoorder',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.positions'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_num',
            field=models.CharField(max_length=6, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('Принят', 'Принят'), ('Готовится', 'Готовится'), ('Отменен', 'Отменен'), ('Готов', 'Готов')], default='Принят', max_length=9, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='positions',
            name='position_name',
            field=models.CharField(max_length=30, verbose_name='Название позиции'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='section_name',
            field=models.CharField(max_length=20, verbose_name='Название категории'),
        ),
    ]