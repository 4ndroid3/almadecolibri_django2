# Django imports
from django.db import models

# Proyect Import

class Producto(models.Model):
    nombre_prd = models.CharField(max_length=30, verbose_name="Nombre Producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey('Categoria_prod', on_delete=models.CASCADE, verbose_name="Categoria")
    imagen_prd = models.ImageField(upload_to = 'productos', blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_prd + ', ' + str(self.precio) + ' los 100g'

class Categoria_prod(models.Model):
    categoria = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categoria Productos'

    def __str__(self):
        return self.categoria