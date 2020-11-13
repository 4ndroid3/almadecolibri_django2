# Django Imports.
from django.http import request
from django.http import response
from django.shortcuts import render

def inicio(request):
    # View del inicio.
    
    return render(request, 'inicio/home.html')