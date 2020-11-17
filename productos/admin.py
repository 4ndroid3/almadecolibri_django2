# Django Imports
from django.contrib import admin

# Project Imports
from productos.models import Producto, Categoria_prod


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre_prd", "id_categoria",)

class CategoriaProdAdmin(admin.ModelAdmin):
    list_display = ("categoria",)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria_prod, CategoriaProdAdmin)