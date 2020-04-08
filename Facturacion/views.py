from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


#Facturar
def facturas_list(request):
    facturas = Factura.objects.all()
    return render(request, 'factura.html', {'facturas': facturas})



#formulario crear factura
def factura_new(request):
    if request.method == "POST":
        formfactura = FacturaForm(request.POST)
        if formfactura.is_valid():
            formfactura.save()

    else:
        formfactura = FacturaForm()
    return render(request, 'facturar.html', {'formfactura': formfactura})



#Facturas detalle
def factura_detalle(request):
    if request.method == "POST":
        formfacturadetail = DetalleFacturaForm(request.POST)
        if formfacturadetail.is_valid():
            formfacturadetail.save()

    else:
        formfacturadetail = DetalleFacturaForm()
    return render(request, 'factura_detalle.html', {'formfacturadetail': formfacturadetail})



def factura_detail(request):
    facturasdetail = DetalleFactura.objects.all()
    return render(request, 'factura_detail.html', {'facturasdetail': facturasdetail})


#necesita id
def factura_detalle(request):
    facturadetalle = DetalleFactura.objects.all()
    return render(request, 'factura_detalle.html', {'facturadetalle': facturadetalle})

