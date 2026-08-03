from django.urls import path
from . import views

urlpatterns = [
    path('registro/<slug:slug>/', views.inscripcion_view, name='inscripcion_evento'),
]