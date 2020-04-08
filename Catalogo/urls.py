from django.urls import path
from . import views

urlpatterns = [

    path('clientes/', views.product_list, name='product_list'),
    path('fabrica/list', views.fabric_list, name='fabric_list'),
    path('vehiculo/list', views.vehiculo_list, name='vehiculo_list'),
    path('product/new/', views.product_new, name='product_new'),
    path('fabric/new/', views.fabric_new, name='fabric_new'),
    path('vehiculo/new/', views.vehiculo_new, name='vehiculo_new'),
    path('product/<int:producto_id>/', views.product_detail, name='product_detail'),
    path('compatibilidad/', views.compatible_list, name='compatibilidad_list'),
    path('compatibilidad/new', views.nueva_compatibilidad, name='comp_new'),
    #path('', views.login, name='login'),
]
