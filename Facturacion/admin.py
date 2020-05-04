from django.contrib import admin
from .models import *

# Register your models here.

class DetalleFacturaInline(admin.TabularInline):
	model = DetalleFactura




class FacturaAdmin(admin.ModelAdmin):

	raw_id_fields = ('nit',)
	inlines = (DetalleFacturaInline,)
	exclude = ['vendedor',]

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.vendedor = request.user
		obj.save()
admin.site.register(Factura, FacturaAdmin)


#Pedidos a Fabrica
class DetallePedidoInline(admin.TabularInline):
	model = DetallePedidos




class PedidosAdmin(admin.ModelAdmin):

	raw_id_fields = ('fabrica',)
	inlines = (DetallePedidoInline,)

	def save_model(self, request, obj, form, change):
		obj.save()
admin.site.register(Pedidos, PedidosAdmin)

