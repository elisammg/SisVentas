from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('nuevopedido', login_required(views.nuevopedido), name='nuevopedido'),
    path('pedidos', login_required(views.pedidos), name='pedidos'),    
    path('detallarpedido', login_required(views.detallarpedido), name='detallarpedido'),
    path('detalle', login_required(views.detalle), name='detalle'),


    path('productosfabrica', login_required(views.consumeAPI), name='productosfabrica'),
    path('pedidosapi', login_required(views.pedidosapi), name='pedidosapi'),

]