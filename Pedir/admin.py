from django.contrib import admin
from .models import *

# Register your models here.

class DetallePedidoInline(admin.TabularInline):
	model = DetallarPedido




class PedidoAdmin(admin.ModelAdmin):

	raw_id_fields = ('fabrica',)
	inlines = (DetallePedidoInline,)
	exclude = ['vendedor',]

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.vendedor = request.user
		obj.save()
admin.site.register(Pedido, PedidoAdmin)