from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import redirect
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


#Compatibilidad
#Lista de compatibles
def compatible_list(request):
   compatibilidad = Relacion.objects.all()
   return render(request, 'Compatibilidad.html', {'compatibilidad': compatibilidad})



def nueva_compatibilidad(request):
    if request.method == "POST":
        formcomp = RelacionForm(request.POST)
        if formcomp.is_valid():
            formcomp.save()
    else:
        formcomp = RelacionForm()
    return render(request, 'compatibilidad_edit.html', {'formcomp': formcomp})




#REST
class VehiculosViewSet (viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('marca')
    serializer_class = VehiculoSerializer
