from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('nuevaorden', login_required(views.nuevaorden), name='nuevaorden'),
    path('ordenes', login_required(views.ordenes), name='ordenes'),    
    path('agregardetalle', login_required(views.agregardetalle), name='agregardetalle'),
    path('detalleorden', login_required(views.detalle), name='detalleorden'),
    path('cobrar', login_required(views.cobrar), name='cobrar'),
    path('cobros', login_required(views.facturas), name='facturas'),


    #Compra credito    
    path('compracredito', login_required(views.nuevofuturo), name='compracredito'),

    #Compra Descuento    
    path('descuento', login_required(views.descuentos), name='descuento'),
    path('pagodesc', login_required(views.pagodesc), name='pagodesc'),

]