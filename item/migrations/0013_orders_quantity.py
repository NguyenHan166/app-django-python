# Generated by Django 4.2.5 on 2023-10-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_alter_orders_time_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]