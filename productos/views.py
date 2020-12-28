# Django Imports
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Sum

# Proyect Imports
from productos.models import Producto
from tienda.models import Venta, Detalle_Venta
from productos.forms import AgregarAlPedido


def productos(request,param=0):
    # View que muestra un resumen de los productos ofrecidos
    def realizar_compra(id_usuario, obtener_precio_final, datos_formulario):
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
            else:
                venta = Venta(
                    id_usuario = id_usuario,
                )
                venta.save()
                # Busco la venta recien creada.
                info_venta = Venta.objects.filter(
                        id_usuario = id_usuario,
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
                # Agrego el precio a la venta.
                venta.precio_total += obtener_precio_final
                venta.save()
    def realizar_compra_invitado(id_usuario, obtener_precio_final, datos_formulario):
        request.session['usuario'] = str(User.objects.get(username= 'invitado'))
        crear_venta = Venta.objects.filter(id_usuario = id_usuario, nombre_inv = request.session.session_key).last()
        print(crear_venta)
        if crear_venta != None:
            try:
                # Primer caso, que crea una venta, 
                # cuando venta finalizada o procesada están True.
                if (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == True):
                    print('picaña1')
                    # Agrego el dato del usuario para que se cree
                    # una nueva venta.
                    
                    venta = Venta(
                        id_usuario = id_usuario,
                        nombre_inv = request.session.session_key,
                    )
                    venta.save()
                    # Busco la venta recien creada.
                    info_venta = Venta.objects.filter(
                            id_usuario = id_usuario,
                            nombre_inv = request.session.session_key, 
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
                    # Agrego el precio a la venta.
                    venta.precio_total += float(obtener_precio_final)
                    venta.save()
                elif (crear_venta.venta_finalizada == False) and (crear_venta.venta_procesada == False):
                    print('picaña2')
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
                    print('picaña3')
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
        else:
            venta = Venta(
                id_usuario = id_usuario,
                nombre_inv = request.session.session_key,
            )
            venta.save()
            # Busco la venta recien creada.
            info_venta = Venta.objects.filter(
                    id_usuario = id_usuario, 
                    nombre_inv = request.session.session_key,
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
            # Agrego el precio a la venta.
            venta.precio_total += obtener_precio_final
            venta.save()
    def ordenar_por_cant_ventas():
        sum_total = Producto.objects.annotate(total_vendido= Sum('detalle_venta__cant_vendida')).order_by('-total_vendido')
        return sum_total
    if request.method == "POST":
        if request.user.is_authenticated:
            dato_usuario = User.objects.get(username= request.user.username)
            formulario_agregar = AgregarAlPedido(request.POST)
            if formulario_agregar.is_valid():
                datos_formulario = formulario_agregar.cleaned_data
                productos = Producto.objects.all()
                obtener_precio_final = (
                    (Producto.objects.get(id=datos_formulario['id_producto']).precio)
                    / 100 ) * datos_formulario['cantidad_a_comprar']
                
                realizar_compra(dato_usuario, obtener_precio_final, datos_formulario)
                            
                context = {
                    'formulario_agregar' : formulario_agregar,
                    'productos': productos,
                }

                return render(request, 'productos/productos.html', context) 
            
            else:
                productos = Producto.objects.all().order_by('nombre_prd')
                formulario_agregar = AgregarAlPedido()
                
                context = {
                    'productos': productos,
                    'formulario_agregar' : formulario_agregar,
                }

                return render(request, 'productos/productos.html', context)
        else:
            
            dato_usuario = User.objects.get(username= 'invitado')
            formulario_agregar = AgregarAlPedido(request.POST)
            if formulario_agregar.is_valid():
                datos_formulario = formulario_agregar.cleaned_data
                productos = Producto.objects.all()
                obtener_precio_final = (
                    (Producto.objects.get(id=datos_formulario['id_producto']).precio)
                    / 100 ) * datos_formulario['cantidad_a_comprar']

            realizar_compra_invitado(dato_usuario, obtener_precio_final, datos_formulario)
            
            formulario_agregar = AgregarAlPedido()
            
            context = {
                'productos': productos,
                'formulario_agregar' : formulario_agregar,
            }

            return render(request, 'productos/productos.html', context)
    else:
        
        # Ordena Alfabeticamente
        if param == 0:
            palabra_buscada = request.GET.get('search_box', '')
            busqueda_producto = Producto.objects.filter(nombre_prd__icontains=palabra_buscada)
        # Ordena por Precio
        elif param == 1:
            palabra_buscada = request.GET.get('search_box', '')
            busqueda_producto = Producto.objects.filter(
                nombre_prd__icontains=palabra_buscada).order_by('-precio')
        # Ordena por Categoria
        elif param == 2:
            palabra_buscada = request.GET.get('search_box', '')
            busqueda_producto = Producto.objects.filter(
                nombre_prd__icontains=palabra_buscada).order_by('id_categoria')    
        elif param == 3:
            palabra_buscada = request.GET.get('search_box', '')
            busqueda_producto = ordenar_por_cant_ventas()

        

        formulario_agregar = AgregarAlPedido()

        context = {
            'productos': busqueda_producto,
            'formulario_agregar' : formulario_agregar,
        }
        
        
        return render(request, 'productos/productos.html', context)
    