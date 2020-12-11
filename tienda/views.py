from django.shortcuts import render
from django.contrib.auth.models import User
import decimal

from productos.models import Producto
from tienda.models import Venta, Detalle_Venta
from tienda.forms import RealizarPedido
from tienda.forms import FinalizarPedido

def tienda(request, param_int=0, param_str=None):
    try:
        dato_usuario = User.objects.get(username= request.user.username)
    except: 
        print('Usuario Deslogueado')
    # View de la tienda de productos
    # funcion que obtiene todoslos datos de una Venta/carrito
    def obtener_carrito():
        try:
            dato_usuario = User.objects.get(username= request.user.username)
            venta = Venta.objects.filter(id_usuario = dato_usuario, venta_finalizada = False).last()
            detalle_venta = Detalle_Venta.objects.filter(id_venta = venta)
            lista_prd = []
            for x in detalle_venta:
                lista_1 = [
                    str(x.id_producto),
                    x.cant_vendida,
                    str(x.precio_unitario),
                    int(venta.id),
                    str(venta.precio_total),
                ]
                lista_prd.append(lista_1)

            return lista_prd
        except:
            print('Usuario Deslogueado')
            
    # Cuando la pagina pide un POST entra al if.
    if request.method == "POST":
        # Obtengo el usuario registrado.
        dato_usuario = User.objects.get(username= request.user.username)
        formularioVenta = RealizarPedido(request.POST)
        # Si se llenaron todos los casilleros del formulario entra al if.
        if formularioVenta.is_valid():
            # Paso los datos del formulario a una variable.
            infoFormulario = formularioVenta.cleaned_data
            # Divido en una lista para obtener los datos del prod.
            #lista_obj_producto = str(infoFormulario['producto'])
            # Obtengo elprecio del producto
            #precio = float(lista_obj_producto)          
            prd_elegido = Producto.objects.filter(nombre_prd= str(infoFormulario['producto']))
           
            # Calculo el precio de lo que compro el usuario.
            precio_final = (infoFormulario['cantidad']/100.00)*float(prd_elegido[0].precio)
            print(infoFormulario['producto'])
            
            # Obtengo el estado de la ultima venta registrada (si existe)
            crear_venta = Venta.objects.filter(id_usuario = dato_usuario).last()
            if crear_venta != None:
            
                try:
                    # Primer caso, que crea una venta, 
                    # cuando venta finalizada o procesada están True.
                    if (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == True):
                        # Agrego el dato del usuario para que se cree
                        # una nueva venta.
                        venta = Venta(
                            id_usuario = dato_usuario,
                        )
                        venta.save()
                        # Busco la venta recien creada.
                        info_venta = Venta.objects.filter(
                                id_usuario = dato_usuario, 
                                venta_finalizada = False, 
                                venta_procesada = False,
                        ).last()
                        print(info_venta)
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
                        print('Error de indice 1')
                except:
                    print('Error de indice 2')
            else:
                venta = Venta(
                    id_usuario = dato_usuario,
                )
                venta.save()
                # Busco la venta recien creada.
                info_venta = Venta.objects.filter(
                        id_usuario = dato_usuario, 
                        venta_finalizada = False, 
                        venta_procesada = False,
                ).last()
                print(info_venta)
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

            finalizar_pedido = FinalizarPedido()
            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(),
                'finalizar_pedido': finalizar_pedido
            }

            if request.method == "POST":
                formularioVenta = RealizarPedido()
                finalizar_pedido = FinalizarPedido()
                
                context = {
                    'formularioVenta': formularioVenta,
                    'lista_ventas': obtener_carrito(),
                    'finalizar_pedido': finalizar_pedido
                }

                return render(request, "tienda/tienda.html", context)

            return render(request, "tienda/tienda.html", context)

        formulario_finalizar = FinalizarPedido(request.POST)
        if formulario_finalizar.is_valid():
            infoFormulario = formulario_finalizar.cleaned_data
            print(infoFormulario)

            finalizar_pedido = Venta.objects.filter(
                id_usuario = dato_usuario,
            ).last()
            if (finalizar_pedido.venta_procesada == False) and (finalizar_pedido.venta_finalizada == False):
                finalizar_pedido.venta_finalizada = infoFormulario['venta_ok']
                finalizar_pedido.save()

            
            formularioVenta = RealizarPedido()
            finalizar_pedido = FinalizarPedido()
                
            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(),
                'finalizar_pedido': finalizar_pedido
            }

        return render(request, "tienda/tienda.html", context)
    else:
        # Condicion para finalizar el pedido con el boton "Finalizar Pedido"
        if param_int == 1:
            finalizar_pedido = Venta.objects.filter(
                id_usuario = dato_usuario,
            ).last()
            if (finalizar_pedido.venta_procesada == False) and (finalizar_pedido.venta_finalizada == False):
                finalizar_pedido.venta_finalizada = True
                finalizar_pedido.save() 

        if param_str != 'safe':
            # Condicion para borrar items de el "carrito"
            # En caso de que el request se esté refiriendo 
            # a otro pedido pongo la palabra safe como seguridad

            # Traigo el N° Venta de
            venta_a_borrar = Venta.objects.filter(id=param_int).last()
            producto = Producto.objects.filter(
                nombre_prd=param_str,
                ).last()
            borrar_art = ''
            try:
                borrar_art = Detalle_Venta.objects.filter(
                    id_venta=venta_a_borrar, 
                    id_producto=producto.id,
                    ).last()
                # Antes de borrar el producto, resto
                # el valor del producto al valor total de la compra.
                venta_a_borrar.precio_total -= borrar_art.precio_unitario
                venta_a_borrar.save()
                borrar_art.delete()
            except:
                print('clase nontype')
            

        formularioVenta = RealizarPedido()
        finalizar_pedido = FinalizarPedido()
        
        context = {
            'formularioVenta': formularioVenta,
            'lista_ventas': obtener_carrito(),
            'finalizar_pedido': finalizar_pedido
        }

    return render(request, "tienda/tienda.html", context)