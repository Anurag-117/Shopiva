# Generated by Django 3.1.2 on 2020-11-16 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orders_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='productImage',
        ),
    ]