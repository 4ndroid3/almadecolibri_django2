# Django Imports
from django.db import models
from django.contrib.auth.models import User

# Project Imports
from productos.models import Producto


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cant_vendida = models.PositiveIntegerField(verbose_name='Cantidad Vendida')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'

    def __str__(self):
        return str(self.id_producto)