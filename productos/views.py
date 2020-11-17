# Django Imports
from django.shortcuts import render

# Proyect Imports
from productos.models import Producto


def productos(request):
    # View que muestra un resumen de los productos ofrecidos
    productos = Producto.objects.all()

    context = {
        'productos': productos,
    }

    return render(request, 'productos/productos.html', context)