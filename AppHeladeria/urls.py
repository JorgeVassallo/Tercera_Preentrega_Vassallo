from django.urls import path
from AppHeladeria.views import *

urlpatterns = [    
    path("crear_clientes/", crear_cliente, name="Crear_cliente"),
    path("crear_sucursales/", crear_sucursal, name="Crear_sucursal"),
    path("crear_sabores/", crear_sabores, name="Crear_sabores"),
    path("buscar_cliente/", buscar_cliente, name="Buscar_cliente"),
    path("buscar_sucursal/", buscar_sucursal, name="Buscar_sucursal"),
    path("buscar_sabor/", buscar_sabor, name="Buscar_sabor"),
    path("ver_clientes/", ver_clientes, name="Clientes"),
    path("ver_sabores/", ver_sabores, name="Sabores"),
    path("ver_sucursales/", ver_sucursales, name="Sucursales"),
    path("", inicio, name="Inicio"),
]