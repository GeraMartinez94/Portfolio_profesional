# core/templatetags/github_extras.py

from django import template
# La importación relativa funciona si views.py está en el mismo nivel que templatetags
# Si da error de importación, usa 'from ..views import get_language_color'
from ..views import get_language_color 

register = template.Library()

@register.filter
def get_language_color_filter(language):
    """Filtro de plantilla para usar la función get_language_color en el HTML."""
    if language:
        return get_language_color(language)
    return "#CCCCCC" # Retorna un color por defecto si es None