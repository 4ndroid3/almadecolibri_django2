from django.shortcuts import render

# Create your views here.
def productos(request):
    # View que muestra un resumen de los productos ofrecidos

    return render(request, 'productos/productos.html')