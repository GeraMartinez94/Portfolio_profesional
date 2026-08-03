from django.urls import path
from . import views

# ¡Importante! El 'app_name' es necesario para la función {% url 'portafolio:detalle' ... %}
app_name = 'portafolio'

urlpatterns = [
    # Esta es una ruta de ejemplo para el detalle del caso de estudio
    path('<slug:slug>/', views.detalle_caso_view, name='detalle'),
    # Deberías crear esta vista 'detalle_caso_view' en views.py
]