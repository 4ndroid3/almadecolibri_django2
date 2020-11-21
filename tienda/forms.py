# Django Imports
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

#App Imports
from productos.models import Producto

class RealizarPedido(forms.Form):
    # crea el formulario para realizar el pedido
    """usuario = forms.ModelChoiceField(
        queryset= User.objects.all(),
        widget=forms.Select(
            attrs = {
                'class':'form-control',
                'placeholder': 'Usuario',
            }
        ) 
    )"""
    producto = forms.ModelChoiceField(
        queryset= Producto.objects.all(),
        widget=forms.Select(
            attrs = {
                'class':'form-control',
                'placeholder': 'Producto',
            }
        )
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {
                'class':'form-control',
                'placeholder': '100g',
            }
        ),
        # Validador, el valor minimo que deja cargar es 1.
        validators=[MinValueValidator(1, message= "rambo")]
    )