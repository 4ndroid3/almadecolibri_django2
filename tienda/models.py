# Django Imports
from django.db import models
from django.contrib.auth.models import User

# Project Imports
from productos.models import Producto



class Venta(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cant_vendida = models.PositiveIntegerField()
    fecha_venta = models.DateField(auto_now_add=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id_usuario)