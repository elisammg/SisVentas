from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


#Clientes

#lista de clientes
def clientes_list(request):
    clientes = cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

#formulario crear cliente
def clientes_new(request):
    if request.method == "POST":
        formclientes = ClienteForm(request.POST)
        if formclientes.is_valid():
            formclientes.save()

    else:
        formclientes = ClienteForm()
    return render(request, 'cliente_edit.html', {'formclientes': formclientes})



#Suscripciones
#lista de suscripciones
def suscripciones(request):
    suscripciones = suscripcion.objects.all()
    return render(request, 'suscripciones.html', {'suscripciones': suscripciones})


#formulario crear fabrica
def suscripcion_new(request):
    if request.method == "POST":
        formsusc = SuscripcionForm(request.POST)
        if formsusc.is_valid():
            formsusc.save()
    else:
        formsusc = SuscripcionForm()
    return render(request, 'suscripcion_new.html', {'formsusc': formsusc})



#Descuentos/Tipo de cliente
#listas de descuentos
def descuentos(request):
   objetos = objeto.objects.all()
   return render(request, 'descuentos.html', {'objetos': objetos})

#formulario crear descuentos
def descuento_new(request):
    if request.method == "POST":
        formdescuento = DescuentoForm(request.POST)
        if formdescuento.is_valid():
            formdescuento.save()
    else:
        formdescuento = DescuentoForm()
    return render(request, 'descuento_new.html', {'formdescuento': formdescuento})
