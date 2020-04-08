from django.urls import path
from . import views

urlpatterns = [

    path('facturas/', views.facturas_list, name='facturas_list'),
    path('facturas/nueva', views.factura_new, name='factura_new'),    
    path('facturas/detalle', views.factura_detalle, name='factura_detalle'),
    path('facturas/detail', views.factura_detail, name='factura_detail'),
]