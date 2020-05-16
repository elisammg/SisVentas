from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator
import urllib.request as ur
import json
# Create your views here.


#Nuevo pedido
def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})



#formulario crear factura
def nuevopedido(request):
    if request.method == "POST":
        formpedido = PedidoForm(request.POST)
        if formpedido.is_valid():
            formpedido.save()

    else:
        formpedido = PedidoForm()
    return render(request, 'nuevopedido.html', {'formpedido': formpedido})


#Nueva detalle pedido
def detalle(request):
    detalles = DetallarPedido.objects.all()
    return render(request, 'detallepedido.html', {'detalles': detalles})



#formulario crear factura
def detallarpedido(request):
    if request.method == "POST":
        formdetalle = DetalleForm(request.POST)
        if formdetalle.is_valid():
            formdetalle.save()

    else:
        formdetalle = DetalleForm()
    return render(request, 'nuevodetalle.html', {'formdetalle': formdetalle})




def consumeAPI(request):
    url = "http://192.168.1.33:8080/rtproductos"
    response = ur.urlopen(url)
    datas = json.loads(response.read())

    return render(request, 'productosfabrica.html', {'datas' : datas})



def pedidosapi(request):
    urlapi = "http://192.168.1.33:8080/pedidosapi"
    responseapi = ur.urlopen(urlapi)
    apipedidos = json.loads(responseapi.read())

    return render(request, 'enviopedido.html', {'apipedidos' : apipedidos})