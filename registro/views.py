from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from registro.forms import SignUpForm
from registro.models import DatosAdicionales


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            telefono = form.cleaned_data.get('telefono')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            dato_usuario = User.objects.get(username= username)
            registrar_tel = DatosAdicionales(
                user=dato_usuario,
                telefono=telefono,)
            registrar_tel.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registro/registro.html', {'form': form})