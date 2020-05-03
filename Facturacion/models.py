from django.db import models
from django.contrib.auth.models import User
import decimal
from django.conf import settings
from django.db.models import signals
from Catalogo.models import *
from Clientes.models import * 
from django.utils import timezone

# Create your models here.





class Factura(models.Model):
    serie = models.IntegerField()
    numero = models.CharField(max_length=6)
    nit = models.ForeignKey(cliente, on_delete= models.CASCADE)
    fecha = models.DateField(auto_now_add = True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return 'Factura: ' + self.numero






class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, db_column='factura_id', related_name='factura', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, db_column='producto_id', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad_venta = models.IntegerField()
    impuesto = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Destalle de Factura: ' + self.descripcion







