# Generated by Django 4.2.1 on 2023-06-08 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=20, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=30, verbose_name='Название позиции')),
                ('position_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Цена позиции')),
                ('Категория', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu.sections')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
    ]
