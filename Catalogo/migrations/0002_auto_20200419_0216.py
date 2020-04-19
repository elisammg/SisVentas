# Generated by Django 2.2 on 2020-04-19 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Fabrica'),
        ),
        migrations.AlterField(
            model_name='relacion',
            name='carro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Vehiculo'),
        ),
        migrations.AlterField(
            model_name='relacion',
            name='repuesto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Producto'),
        ),
    ]
