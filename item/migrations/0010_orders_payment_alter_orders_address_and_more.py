# Generated by Django 4.2.5 on 2023-10-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_orders_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment',
            field=models.CharField(default='cash', max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phonenumber',
            field=models.CharField(default='', max_length=50),
        ),
    ]
