from django import forms

from .models import *

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden 
        fields = '__all__'


        

class DetalleForm(forms.ModelForm):

	class Meta:
		model = Detalle
		fields = {
		'orden': forms.NumberInput,
		'producto':forms.Select,
		'cantidad':forms.NumberInput,
		'descripcion':forms.Textarea,
		}


class FormFac(forms.ModelForm):

    class Meta:
        model = Facturacion 
        fields = ('cliente_nit','orden','total','descripcion',)


class FuturoForm(forms.ModelForm):

    class Meta:
        model = OrdenFuturo 
        fields = '__all__'




class CreditoForm(forms.ModelForm):

    class Meta:
        model = Credito 
        fields = '__all__'




class DescuentoF(forms.ModelForm):

    class Meta:
        model = Descuento 
        fields = '__all__'