from django import forms

from .models import *

class ClienteForm(forms.ModelForm):

    class Meta:
        model = cliente
        fields = ('nit', 'nombre', 'email', 'telefono', 'patente', 'tipo',)


class SuscripcionForm(forms.ModelForm):

    class Meta:
        model = suscripcion
        fields = ('estado', 'fecha_creacion', 'fecha_expiracion', 'cliente',)


class DescuentoForm(forms.ModelForm):

    class Meta:
        model = objeto
        fields = ('nombre', 'descripcion',)

