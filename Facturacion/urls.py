from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('facturas/', login_required(views.facturas_list), name='facturas_list'),
    path('facturas/nueva', login_required(views.factura_new), name='factura_new'),    
    path('facturas/detalle', login_required(views.factura_detalle), name='factura_detalle'),
    path('facturas/detail', login_required(views.factura_detail), name='factura_detail'),
#pedidos
    path('pedidos/', login_required(views.pedidos_list), name='pedidos_list'),
    path('pedidos/nueva', login_required(views.pedido_new), name='pedido_new'),    
    path('pedidos/detalle', login_required(views.pedido_detalle), name='pedido_detalle'),
    path('pedidos/detail', login_required(views.pedido_detail), name='pedido_detail'),
]