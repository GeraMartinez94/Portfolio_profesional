from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # ¡Añade esta línea! 
    path('contacto/', views.contacto_view, name='contacto'), 
    path('api/chat/', views.chat_api, name='chat_api'),
]