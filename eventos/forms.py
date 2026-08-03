# eventos/forms.py

from django import forms
from .models import Inscripcion 

class InscripcionForm(forms.ModelForm):
    # Definimos los campos que se mapearán directamente a tu modelo Inscripcion
    class Meta:
        model = Inscripcion
        # Usamos 'nombre', 'email', y 'empresa'
        fields = ['nombre', 'email', 'empresa'] 
        
        # Agregamos atributos HTML (clases, placeholders)
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu.correo@ejemplo.com', 'class': 'form-control'}),
            # Usamos 'empresa' en lugar de 'rol'
            'empresa': forms.TextInput(attrs={'placeholder': 'Tu Empresa (Opcional)', 'class': 'form-control'}), 
        }
        
        # Personalizar etiquetas
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo Electrónico',
            'empresa': 'Empresa/Organización',
        }