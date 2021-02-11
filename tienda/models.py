# Django Imports
from django.db import models
from django.contrib.auth.models import User

# Project Imports
from productos.models import Producto


class Venta(models.Model):
    """ Clase que maneja las ventas realizadas por los usuarios.
    
    
    
    Contiene:
    - ID
    - ID_Usuario (trae el nombre del usuario que realizo la compra)
    - Nombre Invitado (en caso de que se realice una venta como usuario 
        no registrado este valor almacenará un nombre provisorio puesto
        por el cliente)
    - Apellido Invitado (en caso de que se realice una venta como usuario 
        no registrado este valor almacenará un apellido provisorio puesto
        por el cliente)
    - Teléfono Invitado (en caso de que se realice una venta como usuario 
        no registrado este valor almacenará un teléfono provisorio puesto
        por el cliente)
    - Precio total de la venta ( suma el valor de todos los productos comprados
        en una venta)
    - Venta Procesada (si el usuario finalizo la venta, el administrador ya puede
        procesar el pedido y prepararlo, una vez preparado, se cambia el estado a
        procesado y se le puede avisar al usuario que su pedido está listo)
    - Venta finalizada (Cuando el usuario finaliza el pedido, este parametro
        pasa a True, dandole la indicacion al administrador de que debe preparar
        el pedido)
    """
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_inv = models.CharField(max_length=150, blank=True)
    apellido_inv = models.CharField(max_length=150, blank=True)
    telefono_inv = models.CharField(max_length=150, blank=True)
    fecha_venta = models.DateField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default= 0.0)
    venta_procesada = models.BooleanField(default = False)
    venta_finalizada = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return str(self.id)
        
class Detalle_Venta(models.Model):
    """ Clase que maneja los productos de cada pedido.
    
    Una vez que el usuario agrega un pedido al carrito de compra se relaciona 
    cada Detalle de venta con un id_venta.
    
    - ID Venta (relaciona la venta individual con una ID de venta del usuario)
    - ID Producto ( relaciona el producto con la venta individual)
    - Cantidad Vendida (cantidad en gramos de el producto seleccionado)
    - Precio Unitario (precio del producto cada 100gramos comprados)
    """
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cant_vendida = models.PositiveIntegerField(verbose_name='Cantidad Vendida')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'

    def __str__(self):
        return str(self.id_producto)
