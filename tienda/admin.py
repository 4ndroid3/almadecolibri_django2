# Django Imports
from django.contrib import admin

# Project Imports
from tienda.models import Venta


class VentaAdmin(admin.ModelAdmin):
    list_display = ("id_usuario", "fecha_venta", "id_producto", "cant_vendida", "precio_venta")
    list_filter = ("fecha_venta",)
    date_hierarchy = 'fecha_venta'
    readonly_fields = ('fecha_venta',)

admin.site.register(Venta, VentaAdmin)