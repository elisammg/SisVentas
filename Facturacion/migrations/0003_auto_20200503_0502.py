# Generated by Django 2.2 on 2020-05-03 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0002_auto_20200419_0216'),
        ('Facturacion', '0002_auto_20200419_0216'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='factura',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_envio', models.DateField(auto_now_add=True)),
                ('fecha_entrega', models.DateField()),
                ('estado', models.CharField(choices=[('enviado', 'Enviado'), ('proceso', 'Proceso'), ('entregado', 'Entregado')], max_length=50)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('fabrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Fabrica')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad_pedido', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pedido', models.ForeignKey(db_column='pedidos_id', on_delete=django.db.models.deletion.CASCADE, related_name='pedidios', to='Facturacion.Pedidos')),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Producto')),
            ],
        ),
    ]