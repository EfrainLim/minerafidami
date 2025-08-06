from blog.models import NoticiaBlog
from core.models import ConfiguracionGeneral, RedSocial
from core.helpers import safe_get_queryset, get_comunicados_activos, get_recientes


def global_context(request):
    """Contexto global disponible en todas las plantillas"""
    context = {}
    
    # Configuración general
    context['config'] = ConfiguracionGeneral.objects.first()
    
    # Redes sociales
    context['redes_sociales'] = safe_get_queryset(
        RedSocial.objects.filter(activo=True).order_by('orden'), 
        []
    )
    
    # Noticias recientes para el footer
    context['noticias_recientes'] = get_recientes(NoticiaBlog, limit=2)
    
    # Comunicados para la página principal
    context['comunicados_home'] = get_comunicados_activos('mostrar_en_home', 5)
    
    # Comunicados para popup
    context['comunicados_popup'] = get_comunicados_activos('mostrar_en_popup', 3)
    
    return context 