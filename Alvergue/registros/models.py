from django.db import models


class SalidaMedicamentos(models.Model):
    id = models.AutoField(primary_key=True)
    AsignadoA = models.CharField(max_length=100)
    Fecha = models.CharField(max_length=100)
    Medicamento = models.CharField(max_length=100)
    Cantidad = models.IntegerField()
    archivo2 = models.FileField(upload_to="archivos", null=True, blank=True, verbose_name="Foto de Perfil")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Salida Medicamentos'
        verbose_name_plural = 'Salidas Medicamentos'

    def __str__(self):
        return self.AsignadoA
    

class Medicamentos(models.Model): #Define la estructura de la tabla
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    categoria = models.CharField( max_length=100, verbose_name="Categoria") #Define el tipo de dato y el tamaño
    NombreMedic = models.CharField( max_length=150, verbose_name="Nombre del Medicamento")
    Descripcion = models.TextField() 
    FechaCad = models.CharField( max_length=50, verbose_name="Fecha de Caducidad")
    stock = models.IntegerField( verbose_name="Stock")
    status = models.CharField( max_length=100, verbose_name="Status")
    precio = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ["created"]
    def __str__(self):
        return self.NombreMedic

class Archivos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    NombrePaciente = models.CharField(null=True, max_length=150, verbose_name="Nombre del Paciente")
    Edad = models.IntegerField(null=True, verbose_name="Edad")
    Sexo = models.CharField(null=True, max_length=100, verbose_name="Sexo")
    CURP = models.CharField(null=True, max_length=100, verbose_name="CURP")
    Direccion = models.CharField(null=True, max_length=100, verbose_name="Direccion")
    Telefono = models.CharField(null=True, max_length=100, verbose_name="Telefono")
    Medicamento = models.CharField(null=True, max_length=100, verbose_name="Medicamentos a Tomar")    
    archivo = models.FileField(upload_to="archivos", null=True, blank=True, verbose_name="Identificacion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    update  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["-created"]
        
        def __str__(self):
            return self.archivo