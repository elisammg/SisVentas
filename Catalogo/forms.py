from django import forms
from .models import Producto, Fabrica, Vehiculo, Relacion



class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        
        fields = {
            'nombre': forms.Textarea,
            'descripcion': forms.Textarea,
            'cantidad': forms.NumberInput,
            'precio_compra': forms.NumberInput,
            'precio': forms.NumberInput,
            'no_parte': forms.NumberInput,
            'fabricante': forms.Select, 
            'iva': forms.NumberInput,

        }


class RelacionForm(forms.ModelForm):

    class Meta:
        model = Relacion
        fields = ('relacion', 'carro', 'repuesto',)


class FabricForm(forms.ModelForm):

    class Meta:
        model = Fabrica
        fields = ('nombre', 'ubicacion', 'IP', 'puerto_conexion',)


class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ('marca', 'linea', 'modelo', 'codigo_universal')