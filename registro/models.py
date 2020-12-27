from django.db import models
from django.contrib.auth.models import User

class DatosAdicionales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30, verbose_name='Teléfono')