# Django imports
from django.db import models

# Proyect Import

class Producto(models.Model):
    """ Carga de los productos a la base de datos.
    
    Contiene: 
    Nombre del Producto.
    Precio.
    Categoria (Heredada de la clase Categoria_prod)
    Imagen (se debe tener importada la libreria Pillow)
    Costo (costo del producto, campo creado con el fin de 
            realizar estadisticas de costo / ganancia)
    """
    nombre_prd = models.CharField(max_length=30, verbose_name="Nombre Producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey('Categoria_prod', on_delete=models.CASCADE, verbose_name="Categoria")
    imagen_prd = models.ImageField(upload_to = 'productos', blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.0)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_prd

class Categoria_prod(models.Model):
    """ Clase con las categorias existentes para todos los productos
    
    Tiene como unico campo la Categoria que luego será importada 
    para usarse en Producto)
    """
    categoria = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categoria Productos'

    def __str__(self):
        return self.categoria
