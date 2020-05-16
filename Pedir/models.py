from django.db import models
from django.contrib.auth.models import User
import decimal
from django.conf import settings
from django.db.models import signals
from Catalogo.models import *
from Clientes.models import * 
from django.utils import timezone

# Create your models here.


class Pedido(models.Model):
    fabrica = models.ForeignKey(Fabrica, db_column='fabrica_id', on_delete= models.CASCADE)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add = True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return 'Pedido: ' + self.descripcion



class DetallarPedido(models.Model):
    pedido = models.ForeignKey(Pedido, db_column='Pedido_id', on_delete= models.CASCADE)
    producto = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return 'Detalle Pedido: ' + self.descripcion


