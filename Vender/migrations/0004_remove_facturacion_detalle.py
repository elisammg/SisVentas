# Generated by Django 2.2 on 2020-05-14 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vender', '0003_facturacion_detalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturacion',
            name='detalle',
        ),
    ]