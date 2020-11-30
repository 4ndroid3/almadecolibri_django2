from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser

from productos.models import Producto
from tienda.models import Venta, Detalle_Venta
from tienda.forms import RealizarPedido

def tienda(request):
    # View de la tienda de productos
    # funcion que obtiene todoslos datos de una Venta/carrito
    def obtener_carrito():
        # Obtener carrito, devuelve un resumen de toda la venta.
        dato_usuario = User.objects.get(username= request.user.username)
        # info_venta devuelve una lista, con objectos Venta adentro
        info_venta = Venta.objects.filter(id_usuario= dato_usuario, venta_finalizada= False)
        
        try:
            lista_ventas = Detalle_Venta.objects.filter(id_venta= info_venta[0])
            carrito = []
            precio_final= 0.0
            for re in lista_ventas:
                nueva_lista = []
                
                producto = str(re).split()[0]
                cantidad = str(re).split()[3]
                total = str(re).split()[4]
                nueva_lista.append(producto)
                nueva_lista.append(cantidad)
                nueva_lista.append(total)

                precio_final += float(str(re).split()[4])
                carrito.append(nueva_lista)
            ambos = [carrito, precio_final]
            print(ambos)
        except:
            ambos = ['','Carrito Vacio']

        return ambos

    # Cuando la pagina pide un POST entra al if.
    if request.method == "POST":
        formularioVenta = RealizarPedido(request.POST)
        # Si se llenaron todos los casilleros del formulario entra al if.
        if formularioVenta.is_valid():
            # Paso los datos del formulario a una variable.
            infoFormulario = formularioVenta.cleaned_data
            # Divido en una lista para obtener los datos del prod.
            lista_obj_producto = str(infoFormulario['producto']).split()
            # Obtengo elprecio del producto
            precio = float(lista_obj_producto[1])          
            # Calculo el precio de lo que compro el usuario.
            precio_final = (infoFormulario['cantidad']/100)*precio

            id_usuario = User.objects.get(username= request.user.username)
            # info_venta devuelve una lista, con objetos Venta abiertas.
            info_venta = Venta.objects.filter(id_usuario= id_usuario, venta_finalizada= False)

            venta = Detalle_Venta(
                id_venta = info_venta[0], 
                id_producto = infoFormulario['producto'], 
                cant_vendida = infoFormulario['cantidad'],
                precio_unitario = precio_final
            )

            venta.save()


            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(),
            }

            if request.method == "POST":
                formularioVenta = RealizarPedido()
                
                context = {
                    'formularioVenta': formularioVenta,
                    'lista_ventas': obtener_carrito(),
                }

                return render(request, "tienda/tienda.html", context)

            return render(request, "tienda/tienda.html", context)


    else:
        formularioVenta = RealizarPedido()
        
        
        context = {
            'formularioVenta': formularioVenta,
            'lista_ventas': obtener_carrito(),
        }

    return render(request, "tienda/tienda.html", context)