# eventos/admin.py

from django.contrib import admin
from .models import Conferencia, Inscripcion

class ConferenciaAdmin(admin.ModelAdmin):
    # CORRECCIÓN: Cambiamos 'fecha' por el nombre correcto del campo: 'fecha_hora'
    list_display = ('titulo', 'fecha_hora', 'slug') 
    
    # Esto asegura que el slug se genere automáticamente desde el título
    prepopulated_fields = {'slug': ('titulo',)} 

# Registra tus modelos
admin.site.register(Conferencia, ConferenciaAdmin)
admin.site.register(Inscripcion)