from django import forms

from .models import *


class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura 
        fields = ('serie', 'numero', 'nit', 'total', 'vendedor',)
        


class DetalleFacturaForm(forms.ModelForm):

	class Meta:
		model = DetalleFactura
		fields = ('producto', 'descripcion', 'precio', 'cantidad_venta', 'impuesto', 'subtotal')