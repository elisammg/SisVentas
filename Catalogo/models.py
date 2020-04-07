from django.db import models
from django.utils import timezone

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
    precio = models.IntegerField(default=0)
    no_parte = models.IntegerField(default=0, unique = True)
    fabricante = models.ForeignKey(Fabrica, on_delete=models.PROTECT)

    def _str_(self):
        return self.nombre




class Relacion(models.Model):
    relacion = models.CharField(max_length=200)
    carro = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, default="")
    repuesto = models.ForeignKey(Producto, on_delete=models.PROTECT, default = "")
    def _str_(self):
        return self.relacion