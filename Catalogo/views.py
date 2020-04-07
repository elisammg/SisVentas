from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

#buscador
def buscador(request):
    queryset = request.GET.get("buscar")
    if queryset:
        productos = Post.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(precio__icontains = queryset)
        ).distinct()
    return render(request,'index.html',{'productos':productos})





#Productos

def product_detail(request, producto_id):
    productos = Producto.objects.get(id = producto_id)
    return render(request, 'Catalogo/product_detail.html', {'productos': productos})

#lista de productos
def product_list(request):
    productos = Producto.objects.all()
    return render(request, 'Catalogo/product_list.html', {'productos': productos})

#formulario crear producto
def product_new(request):
    if request.method == "POST":
        formproducto = ProductForm(request.POST)
        if formproducto.is_valid():
            formproducto.save()

    else:
        formproducto = ProductForm()
    return render(request, 'Catalogo/product_edit.html', {'formproducto': formproducto})



#Fabricas
#lista de fabricas
def fabric_list(request):
    fabricas = Fabrica.objects.all()
    return render(request, 'Catalogo/fabric_list.html', {'fabricas': fabricas})


#formulario crear fabrica
def fabric_new(request):
    if request.method == "POST":
        formfabric = FabricForm(request.POST)
        if formfabric.is_valid():
            formfabric.save()
    else:
        formfabric = FabricForm()
    return render(request, 'Catalogo/fabric_edit.html', {'formfabric': formfabric})



#Vehiculos
#listas de vehiculos
def vehiculo_list(request):
   vehiculos = Vehiculo.objects.all()
   return render(request, 'Catalogo/vehiculo_list.html', {'vehiculos': vehiculos})

#formulario crear producto
def vehiculo_new(request):
    if request.method == "POST":
        formvehiculo = VehiculoForm(request.POST)
        if formvehiculo.is_valid():
            formvehiculo.save()
    else:
        formvehiculo = VehiculoForm()
    return render(request, 'Catalogo/vehiculo_edit.html', {'formvehiculo': formvehiculo})


#Compatibilidad
#Lista de compatibles
def compatible_list(request):
   compatibilidad = Relacion.objects.all()
   return render(request, 'Catalogo/Compatibilidad.html', {'compatibilidad': compatibilidad})



def nueva_compatibilidad(request):
    if request.method == "POST":
        formcomp = RelacionForm(request.POST)
        if formcomp.is_valid():
            formcomp.save()
    else:
        formcomp = RelacionForm()
    return render(request, 'Catalogo/compatibilidad_edit.html', {'formcomp': formcomp})