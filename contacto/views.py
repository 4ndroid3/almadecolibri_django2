from django.shortcuts import render

def contacto(request):
    # View de la pagina de contacto.

    return render(request, 'contacto/contacto.html')