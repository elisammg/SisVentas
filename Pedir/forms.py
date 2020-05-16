from django import forms

from .models import *

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido 
        fields = '__all__'


        

class DetalleForm(forms.ModelForm):

	class Meta:
		model = DetallarPedido
		fields = '__all__'
