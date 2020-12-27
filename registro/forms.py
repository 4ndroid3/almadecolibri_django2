from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from registro.models import DatosAdicionales


class SignUpForm(UserCreationForm):
    username = forms.CharField(
            max_length=150, 
            required=True,
            label='Nombre de Usuario',
            help_text='Puede contener letras y numeros.', 
            widget=forms.TextInput(
                    attrs = {
                            'class': 'form-control',
                            'placeholder': 'nombre_usuario_123'
                    }
            )
        )
    first_name = forms.CharField(max_length=30, 
                required=False, 
                help_text='Campo opcional', 
                label = 'Nombre',
                widget=forms.TextInput(
                    attrs = {
                            'class': 'form-control',
                            'placeholder': 'Nombre'
                    }
            )
        )   
    last_name = forms.CharField(
            max_length=30, 
            required=False, 
            help_text='Campo opcional',
            label = 'Apellido',
            widget=forms.TextInput(
                    attrs = {
                            'class': 'form-control',
                            'placeholder': 'Apellido'
                    }
            )
        )
    telefono = forms.CharField(
            max_length=30, 
            help_text='Campo requerido', 
            label='Teléfono',
            widget=forms.TextInput(
                    attrs = {
                            'class': 'form-control',
                            'placeholder': 'ej: 3489426887'
                    }
            )
        )
    email = forms.EmailField(
            max_length=254, 
            help_text='Campo requerido',
            widget=forms.TextInput(
                    attrs = {
                            'class': 'form-control',
                            'placeholder': 'ejemplo@gmail.com'
                    }
            )
        )
    password1 = forms.CharField(
            label='Contraseña', 
            widget=forms.PasswordInput(
                    attrs= {
                            'class': 'form-control'
                    }
            )
        )
    password2 = forms.CharField(
            label='Confirmar Contraseña', 
            widget=forms.PasswordInput(
                    attrs= {
                            'class': 'form-control'
                    }
            )
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )