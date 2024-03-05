from django.shortcuts import render
from django.http import HttpResponse
from AppHeladeria.models import Clientes, Sabores, Sucursales
from AppHeladeria.forms import ClientesFormulario, SaboresFormulario, SucursalesFormulario

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def ver_clientes(request):

    return render(request, "ver_clientes.html")

def ver_sabores(request):

    return render(request, "ver_sabores.html")

def ver_sucursales(request):

    return render(request, "ver_sucursales.html")

def crear_sabores(request):
    if request.method == "POST":
        sabores_formulario = SaboresFormulario(request.POST) # se almacena la info del form
        if sabores_formulario.is_valid():
            sabores_dic = sabores_formulario.cleaned_data #se convierte en diccionario

            sabor_nuevo = Sabores(sabor=sabores_dic["sabor"], 
                                        ingredientes=sabores_dic["ingredientes"], 
                                        disponibilidad=sabores_dic["disponibilidad"]
                                        )
            sabor_nuevo.save()
            return render(request, "inicio.html")
    else:

        sabores_formulario = SaboresFormulario()
    
    return render(request, "crear_sabores.html", {"formu": sabores_formulario})


def crear_cliente(request):

    if request.method == "POST":
        cliente_formulario = ClientesFormulario(request.POST) # se almacena la info del form
        if cliente_formulario.is_valid():
            cliente_dic = cliente_formulario.cleaned_data #se convierte en diccionario

            cliente_nuevo = Clientes(nombre=cliente_dic["nombre"], 
                                        apellido=cliente_dic["apellido"], 
                                        direccion=cliente_dic["direccion"],
                                        telefono=cliente_dic["telefono"],
                                        email=cliente_dic["email"]
                                        )
            cliente_nuevo.save()
            return render(request, "inicio.html")
    else:

        cliente_formulario = ClientesFormulario()
    
    return render(request, "crear_cliente.html", {"formu": cliente_formulario})

def crear_sucursal(request):

    if request.method == "POST":
        sucursal_formulario = SucursalesFormulario(request.POST) # se almacena la info del form
        if sucursal_formulario.is_valid():
            sucursal_dic = sucursal_formulario.cleaned_data #se convierte en diccionario

            sucursal_nueva = Sucursales(direccion=sucursal_dic["direccion"], 
                                        telefono=sucursal_dic["telefono"], 
                                        provincia=sucursal_dic["provincia"]
                                        )
            sucursal_nueva.save()
            return render(request, "inicio.html")
    else:

        sucursal_formulario = SucursalesFormulario()

    return render(request, "crear_sucursal.html", {"formu": sucursal_formulario})

def buscar_cliente(request):

    if request.GET:
        nombre = request.GET["nombre"]
        cliente = Clientes.objects.filter(nombre__icontains=nombre)

        mensaje = f"Buscando cliente {nombre}"  

        return render(request, "buscar_cliente.html", {"mensaje":mensaje, "resultado":cliente})
    
    return render(request, "buscar_cliente.html")

def buscar_sucursal(request):

    if request.GET:
        direccion = request.GET["direccion"]
        sucursal = Sucursales.objects.filter(direccion__icontains=direccion)

        mensaje = f"Buscando sucursal {direccion}"  

        return render(request, "buscar_sucursal.html", {"mensaje":mensaje, "resultado":sucursal})
    
    return render(request, "buscar_sucursal.html")

def buscar_sabor(request):

    if request.GET:
        sabor = request.GET["sabor"]
        saborbusqueda = Sabores.objects.filter(sabor__icontains=sabor)

        mensaje = f"Buscando sabor {sabor}"  

        return render(request, "buscar_sabor.html", {"mensaje":mensaje, "resultado":saborbusqueda})
    
    return render(request, "buscar_sabor.html")