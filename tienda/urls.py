# Django Imports
from django.urls import path

# App Imports
from . import views


urlpatterns = [
    path('',views.tienda, name="Tienda"),
    path('<int:param_int>/<str:param_str>', views.tienda),
]