# Django Imports
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('products/', include('productos.urls')),
    path('shop/', include('tienda.urls')),
    path('contact/', include('contacto.urls')),
]