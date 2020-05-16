from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
from django.contrib.auth.models import User
import decimal
from django.conf import settings
from django.db.models import signals
from Catalogo.models import *
from Clientes.models import * 

# Create your models here.


class Orden(models.Model):
    cliente = models.ForeignKey(cliente, db_column='cliente_nombre', on_delete= models.CASCADE)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return 'Orden: ' + self.descripcion


class OrdenFuturo(models.Model):
	cliente = models.ForeignKey(cliente, db_column='cliente_nombre', on_delete= models.CASCADE)
	vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=50)
	fecha_entrega = models.DateField(auto_now_add = False)

	def __str__(self):
		return 'Orden futuro: ' + self.descripcion



class Detalle(models.Model):
    orden = models.ForeignKey(Orden, db_column='Orden_id', on_delete= models.CASCADE)
    producto = models.ForeignKey(Producto, db_column='Producto_id', on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return 'Detalle: ' + self.descripcion



    def valor(self):
        self.subtotal = self.cantidad * 10
        return self.subtotal
		




class Facturacion(models.Model):
	cliente_nit = models.ForeignKey(cliente, db_column='cliente_nit', on_delete=models.CASCADE)
	orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default=0)
	fecha = models.DateField(auto_now_add = True)
	total = models.FloatField()
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return 'Factura: ' + self.descripcion

	def mayorista(self):
		if self.cliente_nit.tipo == 'mayorista':
			self.total = self.total * 0.75
		return self.total


	def taller(self):
		if self.cliente_nit.tipo == 'taller':
			self.total = self.total * 0.90
		return self.total





class Credito(models.Model):
	cliente_nit = models.ForeignKey(cliente, db_column='cliente_nit', on_delete=models.CASCADE)
	orden = models.ForeignKey(OrdenFuturo, on_delete=models.CASCADE, default=0)
	fecha_actual = models.DateField(auto_now_add = True)
	fecha_pago = models.DateField(auto_now_add = False)
	total = models.FloatField()
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return 'Factura: ' + self.descripcion


class Descuento(models.Model):
	cliente_nit = models.ForeignKey(cliente, db_column='cliente_nit', on_delete=models.CASCADE)
	factura = models.ForeignKey(Facturacion, on_delete=models.CASCADE, default=0)
	porcentaje = models.FloatField()	
	fecha_inicio = models.DateField(auto_now_add = False)
	fecha_final = models.DateField(auto_now_add = False)
	total = models.FloatField()
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return 'Factura: ' + self.descripcion

	def promocion(self):
		self.total = self.total * self.porcentaje
		return self.total







