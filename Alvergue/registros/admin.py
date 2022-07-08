from typing import Optional, Sequence
from django.contrib import admin

from .models import Medicamentos


class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombreMedic', 'clave' ,'stock')
    search_fields: Sequence[str] = ('NombreMedic', 'clave')
    date_hierarchy: Optional[str] = 'created'
    list_filter = ('NombreMedic','categoria')
    

    
admin.site.register(Medicamentos, AdministartModelo)