from blog.models import NoticiaBlog
from core.models import ConfiguracionGeneral, RedSocial
from comunicados.models import Comunicado
from django.utils import timezone
from django.db.models import Q


def global_context(request):
    """Contexto global disponible en todas las plantillas"""
    context = {}
    
    # Configuración general
    try:
        context['config'] = ConfiguracionGeneral.objects.first()
    except:
        context['config'] = None
    
    # Redes sociales
    try:
        context['redes_sociales'] = RedSocial.objects.filter(activo=True).order_by('orden')
    except:
        context['redes_sociales'] = []
    
    # Noticias recientes para el footer
    try:
        context['noticias_recientes'] = NoticiaBlog.objects.filter(
            estado='publicado'
        ).order_by('-fecha_publicacion')[:2]
    except:
        context['noticias_recientes'] = []
    
    # Comunicados para la página principal
    try:
        context['comunicados_home'] = Comunicado.objects.filter(
            mostrar_en_home=True,
            estado='publicado',
            activo=True
        ).filter(
            Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
        ).filter(
            Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
        ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:5]
    except:
        context['comunicados_home'] = []
    
    # Comunicados para popup
    try:
        context['comunicados_popup'] = Comunicado.objects.filter(
            mostrar_en_popup=True,
            estado='publicado',
            activo=True
        ).filter(
            Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
        ).filter(
            Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
        ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:3]
    except:
        context['comunicados_popup'] = []
    
    return context 