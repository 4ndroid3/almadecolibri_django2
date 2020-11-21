# Django Imports
from django.contrib import admin

# Project Imports
from tienda.models import Venta, Detalle_Venta



class VentaAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_venta", "precio_total","venta_finalizada", "procesada")
    list_filter = ("fecha_venta", "procesada")
    ordering = ('-fecha_venta',)
    date_hierarchy = 'fecha_venta'
    readonly_fields = ('fecha_venta',)

class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ("id_venta", "id_usuario", "id_producto", "cant_vendida", "precio_unitario")
    list_filter = ("id_venta", "id_usuario")
    ordering = ('-id_venta',)
    search_fields = ("id_usuario__username",)

admin.site.register(Detalle_Venta, DetalleVentaAdmin)
admin.site.register(Venta, VentaAdmin)