# Generated by Django 2.2 on 2020-04-08 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('patente', models.CharField(max_length=60)),
                ('tipo', models.CharField(choices=[('mayorisat', 'Mayorista'), ('taller', 'Taller'), ('individual', 'Individual')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='suscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('inactiva', 'Inactiva')], max_length=50)),
                ('fecha_expiracion', models.DateField()),
                ('fecha_creacion', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clientes.cliente')),
            ],
        ),
    ]
