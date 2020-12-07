# Django Imports
from django.shortcuts import render
from django.contrib.auth.models import User

# Proyect Imports
from productos.models import Producto
from tienda.models import Venta, Detalle_Venta
from productos.forms import AgregarAlPedido


def productos(request):
    # View que muestra un resumen de los productos ofrecidos
    if request.method == "POST":
        dato_usuario = User.objects.get(username= request.user.username)
        formulario_agregar = AgregarAlPedido(request.POST)
        if formulario_agregar.is_valid():
            datos_formulario = formulario_agregar.cleaned_data
            productos = Producto.objects.all()
            obtener_precio_final = (
                (Producto.objects.get(id=datos_formulario['id_producto']).precio)
                / 100 ) * datos_formulario['cantidad_a_comprar']
            # Obtengo el estado de la ultima venta registrada (si existe)
            crear_venta = Venta.objects.filter(id_usuario = dato_usuario).last()
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
                    
                    # Luego guardo la compra en la nueva venta.
                    detall_venta = Detalle_Venta(
                        id_venta = info_venta, 
                        id_producto = Producto.objects.get(id=datos_formulario['id_producto']), 
                        cant_vendida = datos_formulario['cantidad_a_comprar'],
                        precio_unitario = obtener_precio_final
                    )
                    detall_venta.save()
                    print(obtener_precio_final)
                    # Agrego el precio a la venta.
                    venta.precio_total += float(obtener_precio_final)
                    venta.save()
                    print(obtener_precio_final)
                elif (crear_venta.venta_finalizada == False) and (crear_venta.venta_procesada == False):
                    # Guardola compra en la venta.
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = Producto.objects.get(id=datos_formulario['id_producto']), 
                        cant_vendida = datos_formulario['cantidad_a_comprar'],
                        precio_unitario = obtener_precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += obtener_precio_final
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
                        id_producto = Producto.objects.get(id=datos_formulario['id_producto']), 
                        cant_vendida = datos_formulario['cantidad_a_comprar'],
                        precio_unitario = obtener_precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += obtener_precio_final
                    crear_venta.save()
                else:
                    print('Error de indice 1')
            except:
                print('Error de indice 2')

                        
            context = {
                'formulario_agregar' : formulario_agregar,
                'productos': productos,
            }

            return render(request, 'productos/productos.html', context) 
        
        else:
            productos = Producto.objects.all().order_by('nombre_prd')
            formulario_agregar = AgregarAlPedido()
            ordenar = [
                Producto.objects.all().order_by('-precio'),
                Producto.objects.all().order_by('id_categoria'),
            ]
            context = {
                'productos': productos,
                'formulario_agregar' : formulario_agregar,
                'ordenar': ordenar
            }

            return render(request, 'productos/productos.html', context)


    else:
        productos = Producto.objects.all().order_by('nombre_prd')
        formulario_agregar = AgregarAlPedido()
        ordenar = [
            Producto.objects.all().order_by('-precio'),
            Producto.objects.all().order_by('id_categoria'),
        ]
        context = {
            'productos': productos,
            'formulario_agregar' : formulario_agregar,
            'ordenar': ordenar
        }
        
        
        return render(request, 'productos/productos.html', context)