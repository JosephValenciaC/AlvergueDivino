from django.shortcuts import render

from .models import Medicamentos

def registros(request):
    medicamentos=Medicamentos.objects.all()
    return render(request, 'registros/registros.html', {"medicamentos":medicamentos})