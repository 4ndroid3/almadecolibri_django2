# Generated by Django 3.1.3 on 2020-11-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20201116_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
