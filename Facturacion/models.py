from django.db import models
from apps.Catalogo.models import *
from apps.Clientes.models import * 
from django.utils import timezone

# Create your models here.

class Factura(models.Model):
	nit = models.ForeignKey(cliente, on_delete= models.PROTECT)
    nombre_cliente = models.ForeignKey(cliente, on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add = True)
    productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.ForeignKey(Producto, on_delete=models.PROTECT)
    precio = models.ForeignKey(Producto, on_delete=models.PROTECT)
    no_parte = models.ForeignKey(Producto, on_delete=models.PROTECT)
    estado = models.ForeignKey(suscripcion, on_delete=models.PROTECT)
    precio_final = models.IntegerField(defaul=cantidad*precio)

    def _str_(self):
        return self.nombre_cliente


class Pedidos(models.Model):
    nit = models.ForeignKey(cliente, on_delete= models.PROTECT)
    nombre_cliente = models.ForeignKey(cliente, on_delete=models.PROTECT)
    productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.ForeignKey(Producto, on_delete=models.PROTECT)
    precio = models.ForeignKey(Producto, on_delete=models.PROTECT)
    no_parte = models.ForeignKey(Producto, on_delete=models.PROTECT)
    estado = models.ForeignKey(suscripcion, on_delete=models.PROTECT)
    fecha_pedido = models.DateField()
	fecha_envio = models.DateField()
	fecha_entrega = models.DateField()

    def _str_(self):
        return self.nombre_cliente 


