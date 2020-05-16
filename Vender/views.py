from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


#Nueva orden de compra
def ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'orden.html', {'ordenes': ordenes})



#formulario crear factura
def nuevaorden(request):
    if request.method == "POST":
        formorden = OrdenForm(request.POST)
        if formorden.is_valid():
            formorden.save()

    else:
        formorden = OrdenForm()
    return render(request, 'nuevaorden.html', {'formorden': formorden})


#Detalle de orden
def agregardetalle(request):
    if request.method == "POST":
        formdetalle = DetalleForm(request.POST)
        if formdetalle.is_valid():
            formdetalle.save()

    else:
        formdetalle = DetalleForm()
    return render(request, 'agregardetalle.html', {'formdetalle': formdetalle})


def detalle(request):
    detalles = Detalle.objects.all()
    return render(request, 'listadodetalle.html', {'detalles': detalles})

#Cobrar
def cobrar(request):
    if request.method == "POST":
        formfac = FormFac(request.POST)
        if formfac.is_valid():
            formfac.save()

    else:
        formfac = FormFac()
    return render(request, 'cobrar.html', {'formfac': formfac})


def facturas(request):
    facturas = Facturacion.objects.all()
    return render(request, 'cobros.html', {'facturas': facturas})




#Ordenes a credito
def nuevofuturo(request):
    if request.method == "POST":
        formfuturo = FuturoForm(request.POST)
        if formfuturo.is_valid():
            formfuturo.save()

    else:
        formfuturo = FuturoForm()
    return render(request, 'compracredito.html', {'formfuturo': formfuturo})



#Descuentos
def descuentos(request):
    if request.method == "POST":
        formdesc = DescuentoF(request.POST)
        if formdesc.is_valid():
            formdesc.save()

    else:
        formdesc = DescuentoF()
    return render(request, 'descuentot.html', {'formdesc': formdesc})


def pagodesc(request):
    pagodescs = Descuento.objects.all()
    return render(request, 'pagardesc.html', {'pagodescs': pagodescs})