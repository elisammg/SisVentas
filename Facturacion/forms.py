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