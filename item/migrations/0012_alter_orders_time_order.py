# Generated by Django 4.2.5 on 2023-10-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_orders_time_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='time_order',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]