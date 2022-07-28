
from django import forms
from .models import Archivos
from django.forms import ClearableFileInput, ModelForm

class CustomClearableFieldInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('NombreMedic', 'categoria', 'descripcion', 'fechaCad', 'stock', 'status','precio' ,'archivo')
        widgets = {
            'archivo': CustomClearableFieldInput
        }
class FormEditar(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ['NombreMedic']