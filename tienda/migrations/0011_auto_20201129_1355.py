# Generated by Django 3.1.3 on 2020-11-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_auto_20201129_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
