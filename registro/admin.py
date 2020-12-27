from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from registro.models import DatosAdicionales

class DatosAdicionalesInline(admin.StackedInline):
    model = DatosAdicionales
    can_delete = False
    verbose_name_plural = 'Datos Adicionales'

class UserAdmin(BaseUserAdmin):
    inlines = (DatosAdicionalesInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)