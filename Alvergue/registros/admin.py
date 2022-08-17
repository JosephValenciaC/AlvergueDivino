from typing import Optional, Sequence
from django.contrib import admin
from .models import Archivos, Medicamentos, SalidaMedicamentos


class AdmiistrarSalida(admin.ModelAdmin):
    list_display = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')
    list_filter = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')
    search_fields = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')
    list_per_page = 2
    list_display_links = ('AsignadoA', 'Fecha', 'Medicamento')
    list_editable = ['Cantidad']
   

admin.site.register(SalidaMedicamentos, AdmiistrarSalida)

class AdministarMedicamentos(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('categoria', 'NombreMedic', 'Descripcion', 'FechaCad', 'stock', 'status', 'precio', 'imagen')
    list_filter = ('categoria', 'NombreMedic', 'status' )
    search_fields = ('categoria', 'NombreMedic', 'Descripcion', 'FechaCad', 'stock', 'status', 'precio')
    list_per_page = 2
    list_display_links = ('categoria', 'NombreMedic', 'Descripcion', 'FechaCad', 'status', 'precio')
    list_editable = ['stock']
    
admin.site.register(Medicamentos, AdministarMedicamentos)

class AdministrarArchivcos(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombrePaciente', 'Edad', 'Sexo', 'CURP', 'Direccion', 'Telefono', 'Medicamento')
    date_hierarchy: Optional[str] = 'created'
    list_filter = ('NombrePaciente','Sexo')
    

admin.site.register(Archivos, AdministrarArchivcos)