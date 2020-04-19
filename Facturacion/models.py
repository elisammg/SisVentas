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



    class Meta:
        unique_together = (('serie', 'numero'),)



    def __unicode__(self):
        return (self.serie, self.numero)






class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, db_column='factura_id', related_name='factura', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, db_column='producto_id', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad_venta = models.IntegerField()
    impuesto = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return u'%s' % self.descripcion

    def suma(self):
        return self.cantidad_venta * self.producto.precio


def update_stock(sender, instance, **kwargs):
    instance.producto.cantidad -= instance.cantidad_venta
    instance.producto.save()

signals.post_save.connect(update_stock, sender=DetalleFactura, dispatch_uid="update_stock_count")



