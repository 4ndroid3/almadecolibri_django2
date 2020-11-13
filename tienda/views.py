from django.shortcuts import render

def tienda(request):
    # View de la tienda de productos

    return render(request, 'tienda/tienda.html')