from typing import Optional, Sequence
from django.contrib import admin
from .models import Archivos, Medicamentos, SalidaMedicamentos

class AdmiistrarSalida(admin.ModelAdmin):
    list_display = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')
    list_filter = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')
    search_fields = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')
    list_per_page = 2
    list_display_links = ('AsignadoA', 'Fecha', 'Medicamento', 'Cantidad')

admin.site.register(SalidaMedicamentos, AdmiistrarSalida)

class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombreMedic' ,'stock')
    date_hierarchy: Optional[str] = 'created'
    list_filter = ('NombreMedic','categoria')
    
admin.site.register(Medicamentos, AdministartModelo)

class AdministrarArchivcos(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombrePaciente' ,'Telefono')
    date_hierarchy: Optional[str] = 'created'
    list_filter = ('NombrePaciente','Sexo')

admin.site.register(Archivos, AdministrarArchivcos)