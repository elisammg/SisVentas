from django.urls import path
from . import views

urlpatterns = [

    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/new/', views.clientes_new, name='clientes_new'),
    path('suscripcion/new/', views.suscripcion_new, name='suscripcion_new'),
    path('suscripciones/', views.suscripciones, name='suscripciones'),
    path('descuento/new/', views.descuento_new, name='descuento_new'),
    path('descuentos/', views.descuentos, name='descuentos'),
    
]