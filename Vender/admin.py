from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Orden)
admin.site.register(Detalle)
admin.site.register(Facturacion)
admin.site.register(OrdenFuturo)
admin.site.register(Credito)
admin.site.register(Descuento)
