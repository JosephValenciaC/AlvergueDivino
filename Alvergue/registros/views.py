from email import message
from django.shortcuts import get_object_or_404, render
from .models import Medicamentos, Archivos
from .forms import FormArchivos, FormEditar
from django.contrib import messages 


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            NombreMedic =request.POST['NombreMedic']
            categoria =request.POST['categoria']
            descripcion =request.POST['descripcion']
            fechaCad =request.POST['fechaCad']
            stock =request.POST['stock']
            status =request.POST['status']
            precio =request.POST['precio']
            archivo =request.FILES['archivo']
            insert = Archivos(NombreMedic=NombreMedic, categoria=categoria ,descripcion=descripcion, fechaCad = fechaCad, stock=stock, status = status, precio = precio ,archivo=archivo)
            insert.save()
            medicamentos = Archivos.objects.all()
            return render(request, 'registros/registros.html', {'medicamentos':medicamentos})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/registrarMedicamentos.html', {'archivo':Archivos})

def consultasSQL(request):
    medicamentos=Archivos.objects.raw('SELECT id, NombreMedic, categoria, descripcion, fechaCad, status, archivo FROM registros_archivos')
    return render (request, 'registros/registros.html', {'medicamentos':medicamentos})

def consultarMedicamento(request, id):
    medicamento = Archivos.objects.get(id=id)
    return render(request, 'registros/formSalida.html', {'medicamento': medicamento})

# Editar
def editarSalida(request, id):
    medicamento = get_object_or_404(Archivos, id=id)
    form = FormEditar(request.POST, instance=medicamento)
    if form.is_valid():
        form.save()
        medicamentos = Archivos.objects.all()
        return render(request, 'registros/registros.html', {'medicamentos': medicamentos})
    return render(request, 'registros/formSalida.html', {'medicamento':medicamento })