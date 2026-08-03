from django.contrib import admin
# ¡CRÍTICO! Debes importar 'include'
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí es donde se conecta tu aplicación 'core' con el proyecto.
    # Usa 'include' para delegar las rutas a la app.
    path('', include('core.urls')), 
    path('portafolio/', include('portafolio.urls')),
    path('eventos/', include('eventos.urls')),
]