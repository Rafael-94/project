
from django import forms
from .models import Tarea, Categoria

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria']  # Campos del modelo Tarea que deseas incluir en el formulario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']  # Campo del modelo Categoria que deseas incluir en el formulario
