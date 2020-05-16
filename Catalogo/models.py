from django.db import models
from django.utils.timezone import datetime
from django.utils import timezone
import decimal




# Create your models here.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=200)
    linea = models.CharField(max_length=200, default = 0)
    modelo = models.IntegerField(default=0)
    codigo_universal = models.IntegerField(default=0, unique=True)


    def __str__(self):
        return 'Vehiculo: ' + self.marca


class Fabrica(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=250)
    IP = models.IntegerField(default= 0, unique=True)
    puerto_conexion = models.IntegerField(default= 0, unique=True)


    def __str__(self):
        return 'Fabrica: ' + self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, default = 0)
    cantidad = models.IntegerField(default=0)
    precio_compra = models.FloatField(default=0.00)
    precio= models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    no_parte = models.IntegerField(default=0, unique = True)
    fabricante = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, default=0)


    def __str__(self):
        return 'Producto: ' + self.nombre

    def preciofinal (self):
        self.precio = (self.precio_compra + (self.precio_compra * 0.15) + (self.precio_compra*0.3) + (self.precio_compra*0.05) + (self.precio_compra*0.4)) + (self.precio_compra*0.12)
        return self.precio


        



