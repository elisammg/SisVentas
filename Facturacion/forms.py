from django import forms

from .models import *

class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura 
        fields = ('serie', 'numero', 'nit', 'total', 'vendedor',)
        

class DetalleForm(forms.ModelForm):

	class Meta:
		model = DetalleFactura
		fields = ('factura', 'producto', 'descripcion', 'precio', 'cantidad_venta', 'impuesto', 'subtotal',)





#Pedidos a fabrica
class PedidosForm(forms.ModelForm):

    class Meta:
        model = Pedidos 
        fields = ('fabrica', 'fecha_entrega', 'total', )
        

class DetallePForm(forms.ModelForm):

	class Meta:
		model = DetallePedidos
		fields = ('pedido', 'producto', 'descripcion', 'cantidad_pedido', 'subtotal',)
