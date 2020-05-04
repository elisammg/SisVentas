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
        formdetail = DetalleForm(request.POST)
        if formdetail.is_valid():
            formdetail.save()

    else:
        formdetail = DetalleForm()
    return render(request, 'factura_detalle.html', {'formdetail': formdetail})



def factura_detail(request):
    facturasdetail = DetalleFactura.objects.all()
    return render(request, 'factura_detail.html', {'facturasdetail': facturasdetail})







#Pedidos a Fabrica
def pedidos_list(request):
    pedido = Pedidos.objects.all()
    return render(request, 'pedidos.html', {'pedido': pedido})



#formulario crear factura
def pedido_new(request):
    if request.method == "POST":
        formpedido = PedidosForm(request.POST)
        if formpedido.is_valid():
            formpedido.save()

    else:
        formpedido = PedidosForm()
    return render(request, 'pedir.html', {'formpedido': formpedido})



#Facturas detalle
def pedido_detalle(request):
    if request.method == "POST":
        formpd = DetallePForm(request.POST)
        if formpd.is_valid():
            formpd.save()

    else:
        formpd = DetallePForm()
    return render(request, 'pedido_detalle.html', {'formpd': formpd})



def pedido_detail(request):
    pdetail = DetallePedidos.objects.all()
    return render(request, 'pedido_detail.html', {'pdetail': pdetail})
