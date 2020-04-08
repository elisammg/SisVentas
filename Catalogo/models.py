from django.db import models
from django.utils import timezone
import decimal

TAX_VALUE = 0.12

# Create your models here.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=200)
    linea = models.CharField(max_length=200, default = 0)
    modelo = models.IntegerField(default=0)
    codigo_universal = models.IntegerField(default=0, unique=True)


    def _str_(self):
        return self.marca


class Fabrica(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=250)
    IP = models.IntegerField(default= 0, unique=True)
    puerto_conexion = models.IntegerField(default= 0, unique=True)


    def _str_(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, default = 0)
    cantidad = models.IntegerField(default=0)
    precio_compra = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    precio= models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    no_parte = models.IntegerField(default=0, unique = True)
    fabricante = models.ForeignKey(Fabrica, on_delete=models.PROTECT)
    iva = models.DecimalField(max_digits=6, decimal_places=3, default=0.000)


    def _str_(self):
        return self.nombre

    def preciototal(self):
        precio_total = self.precio_compra * self.cantidad
        return precio_total


    def incrementarcantidad(self, *args, **kwargs):
        if self.cantidad == 0:
            self.cantidad += 1
            self.store.save()
        super(Producto, self).save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if self.precio:
            self.iva = round(float(self.precio) * TAX_VALUE, 3)
            super(Producto, self).save(*args, **kwargs)
        else:
            self.iva=0
            super(Producto, self).save(*args, **kwargs)



class Relacion(models.Model):
    relacion = models.CharField(max_length=200)
    carro = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, default="")
    repuesto = models.ForeignKey(Producto, on_delete=models.PROTECT, default = "")
    def _str_(self):
        return self.relacion