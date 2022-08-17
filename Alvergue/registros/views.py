from email import message
from django.shortcuts import get_object_or_404, render
from .models import Medicamentos, Archivos, SalidaMedicamentos
from .forms import FormArchivos, FormEditar, SalidaForm
from django.contrib import messages 

def medicamentos(request):
    medicamentos = Medicamentos.objects.all()
    return render(request, 'registros/registros.html', {'medicamentos': medicamentos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            NombrePaciente =request.POST['NombrePaciente']
            Edad =request.POST['Edad']
            Sexo =request.POST['Sexo']
            CURP =request.POST['CURP']
            Direccion =request.POST['Direccion']
            Telefono =request.POST['Telefono']
            Medicamento =request.POST['Medicamento']
            archivo =request.FILES['archivo']
            insert = Archivos(NombrePaciente=NombrePaciente, Edad=Edad ,Sexo=Sexo, CURP = CURP, Direccion=Direccion, Telefono = Telefono, Medicamento = Medicamento ,archivo=archivo)
            insert.save()
            pacientes = Archivos.objects.all()
            return render(request, 'registros/pacientes.html', {'pacientes':pacientes})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/registrarPaciente.html', {'archivo':Archivos})

def consultaSQL(request):
    pacientes=Archivos.objects.raw('SELECT id, NombrePaciente, Edad, Sexo, CURP, Direccion, Telefono, Medicamento, archivo  FROM registros_archivos')
    return render (request, 'registros/pacientes.html', {'pacientes':pacientes})

def consultarPaciente(request, id):
    medicamento = Archivos.objects.get(id=id)
    return render(request, 'registros/formPaciente.html', {'medicamento': medicamento})

# Editar
def editarPaciene(request, id):
    paciente = get_object_or_404(Archivos, id=id)
    form = FormEditar(request.POST, instance=paciente)
    if form.is_valid():
        form.save()
        pacientes = Archivos.objects.all()
        return render(request, 'registros/pacientes.html', {'pacientes': pacientes})
    return render(request, 'registros/formPacientea.html', {'paciente':paciente })

def eliminar(request, id, confirmacion = 'registros/confirmarEliminacion.html'):
    paciente = get_object_or_404(Archivos, id=id)
    if request.method == 'POST':
        paciente.delete()
        pacientes = Archivos.objects.all()
        return render(request, 'registros/pacientes.html', {'pacientes': pacientes})
    return render(request, confirmacion, {'object': paciente})


def stock(request):
    medicamentos = Medicamentos.objects.filter(stock__lte=5)
    return render(request, 'registros/registros.html', {'medicamentos': medicamentos})

def registrarSalida(request):
    return render(request, 'registros/registroSalida.html')

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            NombrePaciente =request.POST['NombrePaciente']
            Edad =request.POST['Edad']
            Sexo =request.POST['Sexo']
            CURP =request.POST['CURP']
            Direccion =request.POST['Direccion']
            Telefono =request.POST['Telefono']
            Medicamento =request.POST['Medicamento']
            archivo =request.FILES['archivo']
            insert = Archivos(NombrePaciente=NombrePaciente, Edad=Edad ,Sexo=Sexo, CURP = CURP, Direccion=Direccion, Telefono = Telefono, Medicamento = Medicamento ,archivo=archivo)
            insert.save()
            pacientes = Archivos.objects.all()
            return render(request, 'registros/pacientes.html', {'pacientes':pacientes})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/registrarPaciente.html', {'archivo':Archivos})


def Salida(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES)
        if form.is_valid():
            AsignadoA =request.POST['AsignadoA']
            Fecha =request.POST['Fecha']
            Medicamento =request.POST['Medicamento']
            Cantidad =request.POST['Cantidad']
            archivo2 =request.FILES['archivo2']
            insert = SalidaMedicamentos(AsignadoA=AsignadoA, Fecha=Fecha , Medicamento = Medicamento, Cantidad=Cantidad, archivo2=archivo2)
            insert.save()
            salidas = SalidaMedicamentos.objects.all()
            return render(request, 'registros/salida.html', {'salidas':salidas})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/registroSalida.html', {'salida':SalidaMedicamentos})

def SalidaSQL(request):
    salidas=SalidaMedicamentos.objects.raw('SELECT id, AsignadoA, Fecha,  Cantidad, archivo2  FROM registros_salidaMedicamentos')
    return render (request, 'registros/salida.html', {'salidas':salidas})
