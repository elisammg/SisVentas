from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('clientes/', login_required(views.clientes_list), name='clientes_list'),
    path('clientes/new/', login_required(views.clientes_new), name='clientes_new'),
    path('suscripcion/new/', login_required(views.suscripcion_new), name='suscripcion_new'),
    path('suscripciones/', login_required(views.suscripciones), name='suscripciones'),
    path('descuento/new/', login_required(views.descuento_new), name='descuento_new'),
    path('descuentos/', login_required(views.descuentos), name='descuentos'),
    
]