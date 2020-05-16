from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail, send_mass_mail
from . import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import View
from django.contrib import messages



# Create your views here.


#Clientes

#lista de clientes
def clientes_list(request):
    clientes = cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})


class CreateClienteView(CreateView): # new
    model = cliente
    form_class = ClienteForm
    template_name = 'cliente_edit.html'
    success_url = reverse_lazy('clientes_list')



#Editar Clientes
class ClientesUpdate(UpdateView): 
    # specify the model you want to use 
    model = cliente 
    
    fields = [
        "nit",
        "nombre",
        "email",
        "telefono",
        "patente",
        "tipo",
    ]

    success_url ="clientes/"


#Eliminar Clientes
class ClienteDelete(DeleteView): 
    # specify the model you want to use 
    model = cliente 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="clientes/"






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


#Editar Clientes
class suscripcionsUpdate(UpdateView): 
    # specify the model you want to use 
    model = suscripcion 
    
    fields = [ 
        "estado",
        "fecha_expiracion",
        "fecha_creacion",
        "cliente",
    ]

    success_url ="clientes/"


#Eliminar Clientes
class suscripcionDelete(DeleteView): 
    # specify the model you want to use 
    model = suscripcion
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="clientes/"    



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



#Mail
class SendFormEmail(View):

    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject', 
            message, 
            'elisamargarita.2899@gmail.com', # Admin
            [
                email,
            ]
        ) 

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('mail') 

