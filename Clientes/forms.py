from django import forms

from .models import *

class ClienteForm(forms.ModelForm):

    class Meta:
        model = cliente
        fields = ['nit', 'nombre', 'email', 'telefono', 'patente', 'tipo']


class SuscripcionForm(forms.ModelForm):

    class Meta:
        model = suscripcion
        fields = ('cliente', 'fecha_expiracion', 'precio')


