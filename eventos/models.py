#eventos/models.py

from django.db import models
from django.utils.text import slugify

class Conferencia(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250, blank=True)
    descripcion_corta = models.CharField(max_length=250)
    descripcion_detallada = models.TextField()
    fecha_hora = models.DateTimeField()
    url_streaming = models.URLField(blank=True, null=True, help_text="Enlace al webinar/meet.")
    ponente = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Inscripcion(models.Model):
    conferencia = models.ForeignKey(Conferencia, on_delete=models.CASCADE, related_name='inscripciones')
    nombre = models.CharField(max_length=100)
    email = models.EmailField() 
    empresa = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} inscrito en {self.conferencia.titulo}"
    
    class Meta:
        unique_together = ('conferencia', 'email')