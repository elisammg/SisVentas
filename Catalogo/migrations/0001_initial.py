# Generated by Django 2.2 on 2020-04-07 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(max_length=250)),
                ('IP', models.IntegerField(default=0, unique=True)),
                ('puerto_conexion', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(default=0, max_length=200)),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('no_parte', models.IntegerField(default=0, unique=True)),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Catalogo.Fabrica')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('linea', models.CharField(default=0, max_length=200)),
                ('modelo', models.IntegerField(default=0)),
                ('codigo_universal', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relacion', models.CharField(max_length=200)),
                ('carro', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='Catalogo.Vehiculo')),
                ('repuesto', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='Catalogo.Producto')),
            ],
        ),
    ]
