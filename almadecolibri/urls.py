# Django Imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Project Imports
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('productos/', include('productos.urls')),
    path('shop/', include('tienda.urls')),
    path('contacto/', include('contacto.urls')),
    path('register/', include('registro.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]