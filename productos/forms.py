# Django Imports
from django import forms
from django.forms.widgets import HiddenInput

# Project Imports


class AgregarAlPedido(forms.Form):
    # Formulario para la ventana modal que se abre 
    # al agregar un elemento al carrito de compras.
    cantidad_a_comprar = forms.IntegerField(
        widget=forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'ej: 100g'
            }
        )
    )
    id_producto = forms.IntegerField(
        widget=forms.HiddenInput(
            attrs= {
                'class':'form-control',
                'value':'0',
                }
            )
        )