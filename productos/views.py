# Django Imports
from django.shortcuts import render

# Proyect Imports
from productos.models import Producto
from productos.forms import AgregarAlPedido


def productos(request):
    # View que muestra un resumen de los productos ofrecidos
    
    if request.method == "POST":
        formulario_agregar = AgregarAlPedido(request.POST)
        if formulario_agregar.is_valid():
            datos_formulario = formulario_agregar.cleaned_data
            productos = Producto.objects.all()
            print(datos_formulario)
            print(productos)
            context = {
                'formulario_agregar' : formulario_agregar
            }

            return render(request, 'productos/productos.html', context)
    else:
        productos = Producto.objects.all()
        formulario_agregar = AgregarAlPedido()
        context = {
            'productos': productos,
            'formulario_agregar' : formulario_agregar
        }

    return render(request, 'productos/productos.html', context)