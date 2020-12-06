from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
import decimal

from productos.models import Producto
from tienda.models import Venta, Detalle_Venta
from tienda.forms import RealizarPedido
from tienda.forms import FinalizarPedido

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
            precio_final = (infoFormulario['cantidad']/100.00)*precio

            # Obtengo el usuario registrado.
            dato_usuario = User.objects.get(username= request.user.username)
            # Obtengo el estado de la ultima venta registrada (si existe)
            crear_venta = Venta.objects.filter(id_usuario = dato_usuario).last()
            
            try:
                # Primer caso, que crea una venta, 
                # cuando venta finalizada o procesada están True.
                if (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == True):
                    print('roñita')
                    # Agrego el dato del usuario para que se cree
                    # una nueva venta.
                    venta = Venta(
                        id_usuario = dato_usuario,
                    )
                    # Busco la venta recien creada.
                    info_venta = Venta.objects.filter(
                            id_usuario = dato_usuario, 
                            venta_finalizada = False, 
                            venta_procesada = False,
                    ).last()
                    # Luego guardo la compra en la nueva venta.
                    detall_venta = Detalle_Venta(
                        id_venta = info_venta, 
                        id_producto = infoFormulario['producto'], 
                        cant_vendida = infoFormulario['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    venta.precio_total += precio_final
                    venta.save()
                elif (crear_venta.venta_finalizada == False) and (crear_venta.venta_procesada == False):
                    # Guardola compra en la venta.
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = infoFormulario['producto'], 
                        cant_vendida = infoFormulario['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += decimal.Decimal(precio_final)
                    crear_venta.save()
                elif (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == False):
                    # Busco si el usuario tiene 
                    # venta finalizada pero no procesada.
                    # Y la cambio a False
                    crear_venta.venta_finalizada = False
                    crear_venta.save()
                    # Agrego el nuevo producto
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = infoFormulario['producto'], 
                        cant_vendida = infoFormulario['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += decimal.Decimal(precio_final)
                    crear_venta.save()
                else:
                    print('Error de indice')
            except:
                print('Error de indice')

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

        if FinalizarPedido.is_valid():
            infoFormulario = FinalizarPedido.cleaned_data
            print(infoFormulario)
        else:
            formularioVenta = RealizarPedido()
            finalizar_pedido = FinalizarPedido()
            
            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(),
                'finalizar_pedido': finalizar_pedido
            }

            return render(request, "tienda/tienda.html", context)
    else:
        # Pruebas
        
        # Finpruebas
        formularioVenta = RealizarPedido()
        finalizar_pedido = FinalizarPedido()
        
        context = {
            'formularioVenta': formularioVenta,
            'lista_ventas': obtener_carrito(),
            'finalizar_pedido': finalizar_pedido
        }

    return render(request, "tienda/tienda.html", context)