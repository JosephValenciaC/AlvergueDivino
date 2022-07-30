from typing import Optional, Sequence
from django.contrib import admin

from .models import Archivos, Medicamentos

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