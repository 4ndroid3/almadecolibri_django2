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
            print('macoña')
            datos_formulario = formulario_agregar.cleaned_data
            productos = Producto.objects.all()
            print('sacacorcho')
            print(datos_formulario)
            print('sacacorcho')
                        
            context = {
                'formulario_agregar' : formulario_agregar,
                'productos': productos,
            }
            print('babamil')
            return render(request, 'productos/productos.html', context) 

    else:
        productos = Producto.objects.all()
        asd = AgregarAlPedido()
        print('merca')

        formulario_agregar = AgregarAlPedido()
        context = {
            'productos': productos,
            'formulario_agregar' : formulario_agregar
        }
        
        
        return render(request, 'productos/productos.html', context)