from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import redirect, render
import urllib.request as ur
import json
from django.views.generic import TemplateView
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
from .forms import *
from rest_framework import viewsets
from .serializers import VehiculoSerializer

# Create your views here.


#Productos

def product_detail(request, producto_id):
    productos = Producto.objects.get(id = producto_id)
    return render(request, 'product_detail.html', {'productos': productos})

#lista de productos
def product_list(request):    
    productos = Producto.objects.all()
    queryset = request.GET.get("buscar")
    print(queryset)
    if queryset:
        productos = Producto.objects.filter(
            Q(nombre__icontains = queryset)
            ).distinct()
    return render(request, 'product_list.html', {'productos': productos})

#formulario crear producto
def product_new(request):
    if request.method == "POST":
        formproducto = ProductForm(request.POST)
        if formproducto.is_valid():
            formproducto.save()

    else:
        formproducto = ProductForm()
    return render(request, 'product_edit.html', {'formproducto': formproducto})



#Editar productos
class ProductosUpdate(UpdateView): 
    # specify the model you want to use 
    model = Producto 
    
    fields = [ 
        "nombre",
        "descripcion",
        "cantidad",
        "precio",
        "no_parte",
        "fabricante",
    ]

    success_url ="/tienda/productos"




#Eliminar producto
class ProductoDelete(DeleteView): 
    # specify the model you want to use 
    model = Producto 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="/tienda/productos"





#Fabricas
#lista de fabricas
def fabric_list(request):
    fabricas = Fabrica.objects.all()
    return render(request, 'fabric_list.html', {'fabricas': fabricas})


#formulario crear fabrica
def fabric_new(request):
    if request.method == "POST":
        formfabric = FabricForm(request.POST)
        if formfabric.is_valid():
            formfabric.save()
    else:
        formfabric = FabricForm()
    return render(request, 'fabric_edit.html', {'formfabric': formfabric})


#Editar fabrica
class FabricasUpdate(UpdateView): 
    # specify the model you want to use 
    model = Fabrica 
    
    fields = [ 
        "nombre",
        "ubicacion",
        "IP",
        "puerto_conexion",
    ]

    success_url ="/tienda/fabrica/list"




#Eliminar fabrica
class FabricaDelete(DeleteView): 
    # specify the model you want to use 
    model = Fabrica 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="/tienda/fabrica/list"






#Vehiculos
#listas de vehiculos
def vehiculo_list(request):
   vehiculos = Vehiculo.objects.all()
   return render(request, 'vehiculo_list.html', {'vehiculos': vehiculos})

#formulario crear producto
def vehiculo_new(request):
    if request.method == "POST":
        formvehiculo = VehiculoForm(request.POST)
        if formvehiculo.is_valid():
            formvehiculo.save()
    else:
        formvehiculo = VehiculoForm()
    return render(request, 'vehiculo_edit.html', {'formvehiculo': formvehiculo})



#Editar Vehiculo
class VehiculosUpdate(UpdateView): 
    # specify the model you want to use 
    model = Vehiculo 
    
    fields = [ 
        "marca",
        "linea",
        "modelo",
        "codigo_universal",
    ]

    success_url ="/tienda/vehiculo/list"




#Eliminar Vehiculo
class VehiculoDelete(DeleteView): 
    # specify the model you want to use 
    model = Vehiculo 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="/tienda/vehiculo/list"


#REST
class VehiculosViewSet (viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('marca')
    serializer_class = VehiculoSerializer



def consumeAPI(request):
    url = "http://192.168.1.30:8080/rtproductos"
    response = ur.urlopen(url)
    datas = json.loads(response.read())

    return render(request, 'productosapi.html', {'datas' : datas})


def APIcarro(request):
    urlcarro = "http://192.168.1.30:8080/carroapi"
    responsecarro = ur.urlopen(urlcarro)
    carros = json.loads(responsecarro.read())

    return render(request, 'carrosapi.html', {'carros' : carros})



