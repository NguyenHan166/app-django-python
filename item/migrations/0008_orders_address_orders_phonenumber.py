# Generated by Django 4.2.5 on 2023-10-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='orders',
            name='phonenumber',
            field=models.CharField(default='', max_length=100),
        ),
    ]
