# Django Imports.
from django.http import request
from django.http import response
from django.shortcuts import render
from django.db.models import Sum

# Proyect Imports
from productos.models import Producto

def inicio(request):
    # View del inicio.
    def ordenar_por_cant_ventas():
        # Funcion que me devuelve los productos más vendidos de la pag.
        sum_total = Producto.objects.annotate(total_vendido= Sum('detalle_venta__cant_vendida')).order_by('-total_vendido')
        return sum_total

    sasa = ordenar_por_cant_ventas()
    top_4 = [
        Producto.objects.get(nombre_prd=sasa[0]),
        Producto.objects.get(nombre_prd=sasa[1]),
        Producto.objects.get(nombre_prd=sasa[2]),
        Producto.objects.get(nombre_prd=sasa[3]),
    ]
    context = {
        'mas_vendidos': top_4,
    }
    
    return render(request, 'inicio/home.html', context)