from django.shortcuts import render, get_object_or_404
from .models import CasoEstudio

# Vista de ejemplo, necesaria para que el enlace en la home funcione.
def detalle_caso_view(request, slug):
    caso = get_object_or_404(CasoEstudio, slug=slug)
    context = {'caso': caso}
    # Asegúrate de crear este archivo de plantilla
    return render(request, 'portafolio/detalle_caso.html', context)