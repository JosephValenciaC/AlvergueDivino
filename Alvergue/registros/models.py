from django.db import models



class Medicamentos(models.Model): #Define la estructura de la tabla
    
    categoria = models.CharField( max_length=100, verbose_name="Categoria") #Define el tipo de dato y el tamaño
    NombreMedic = models.CharField( max_length=150, verbose_name="Nombre del Medicamento")
    Descripcion = models.TextField() 
    clave = models.CharField( max_length=150, verbose_name="Clave")
    FechaCad = models.CharField( max_length=50, verbose_name="Fecha de Caducidad")
    stock = models.IntegerField( verbose_name="Stock")
    status = models.CharField( max_length=100, verbose_name="Status")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ["created"]
    def __str__(self):
        return self.categoria