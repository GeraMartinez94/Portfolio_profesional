from django.db import models
from django.utils.text import slugify

class CasoEstudio(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250, blank=True)
    nicho_cliente = models.CharField(max_length=100, help_text="Ej: FinTech, LegalTech")
    problema = models.TextField()
    solucion_ia = models.TextField(verbose_name="Solución Implementada (LLM/IA)")
    resultado_clave = models.TextField(help_text="Métrica cuantificable: Ej: 30% reducción de latencia.")
    enlace_github = models.URLField(blank=True, null=True, verbose_name="GitHub del POC")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo