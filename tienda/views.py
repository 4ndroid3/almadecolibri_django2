from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser

from productos.models import Producto
from tienda.models import Venta
from tienda.forms import RealizarPedido

def tienda(request):
    # View de la tienda de productos
    # Cuando la pagina pide un POST entra al if.
    if request.method == "POST":
        formularioVenta = RealizarPedido(request.POST)
        # Si se llenaron todos los casilleros del formulario entra al if.
        if formularioVenta.is_valid():
            # Paso los datos del formulario a una variable.
            infoFormulario = formularioVenta.cleaned_data
            # Traigo los productos de la base, para extrar el precio.
            productos = Producto.objects.all()
            for producto in productos:
                # Cuando aparezca el producto de la db que coincide con el 
                # ingresado en la compra.
                if producto == infoFormulario['producto']:
                    # paso la info de DB a string y luego a lista para extraer el precio.
                    lista_producto = str(producto).split()
            
            for precio_producto in lista_producto:
                # Analizo el contenido de la lista
                try:
                    # Si encuentro una variable que se pueda convertir
                    #  en float interrumpo el loop.
                    precio_float = float(precio_producto)
                    break
                except:
                    precio_float = 0.0
            # Calculo el precio de lo que compro el usuario.
            precio_final = (infoFormulario['cantidad']/100)*precio_float
            
            venta = Venta(
                id_usuario = User.objects.get(username= request.user.username),
                id_producto = infoFormulario['producto'], 
                cant_vendida = infoFormulario['cantidad'],
                precio_venta = precio_final
            )

            venta.save()

            mensaje = "Gracias"

            context = {
                'formularioVenta': formularioVenta,     
            }

            if request.method == "POST":
                return render(request, "tienda/tienda.html", {'mensaje': mensaje})

            return render(request, "tienda/tienda.html", context)


    else:
        formularioVenta = RealizarPedido()

    return render(request, "tienda/tienda.html", {"formularioVenta": formularioVenta})