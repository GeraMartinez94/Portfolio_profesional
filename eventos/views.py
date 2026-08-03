# eventos/views.py

from django.shortcuts import render # Ya no necesitamos get_object_or_404
# from .models import Conferencia, Inscripcion # Si ya no usas estos modelos, puedes comentar o eliminar la importación
# from .forms import InscripcionForm

# La vista ahora IGNORA el slug que recibe, ya que la plantilla será estática.
# Mantenemos el argumento 'slug' porque la URL lo envía, pero no lo usamos.
def inscripcion_view(request, slug):
    """
    Simplemente muestra la página de agendamiento de Calendly,
    eliminando la dependencia de buscar el objeto 'Conferencia' en la DB.
    """

    # NOTA: Ya no llamamos a get_object_or_404(Conferencia, slug=slug)

    # Puedes pasar un título fijo si lo deseas, o dejar que la plantilla lo muestre estáticamente
    context = {
        'titulo_pagina': 'Agenda tu Charla de 15 Minutos' 
    }
    
    # La plantilla inscripcion.html ahora es la página de agendamiento con Calendly.
    return render(request, 'eventos/inscripcion.html', context)