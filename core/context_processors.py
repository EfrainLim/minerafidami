from blog.models import NoticiaBlog
from core.models import ConfiguracionGeneral, RedSocial, EnlaceExterno
from core.helpers import safe_get_queryset, get_comunicados_activos, get_recientes


def global_context(request):
    """Context processor global para toda la aplicación"""
    try:
        config = ConfiguracionGeneral.objects.first()
    except:
        config = None
    
    try:
        enlaces_externos = EnlaceExterno.objects.filter(activo=True).order_by('orden', 'nombre')
    except:
        enlaces_externos = []
    
    try:
        # Comunicados para la página principal
        from comunicados.models import Comunicado
        from django.utils import timezone
        from django.db.models import Q
        
        comunicados_home = Comunicado.objects.filter(
            mostrar_en_home=True,
            estado='publicado',
            activo=True
        ).filter(
            Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
        ).filter(
            Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
        ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:3]
    except:
        comunicados_home = []
    
    try:
        # Comunicados para popup
        from comunicados.models import Comunicado
        from django.utils import timezone
        from django.db.models import Q
        
        comunicados_popup = Comunicado.objects.filter(
            mostrar_en_popup=True,
            estado='publicado',
            activo=True
        ).filter(
            Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
        ).filter(
            Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
        ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:5]
    except:
        comunicados_popup = []
    
    try:
        # Noticias recientes para el footer
        noticias_recientes = NoticiaBlog.objects.filter(
            estado='publicado'
        ).order_by('-fecha_publicacion')[:3]
    except:
        noticias_recientes = []
    
    try:
        # Redes sociales para el footer
        redes_sociales = RedSocial.objects.filter(activo=True).order_by('orden')
    except:
        redes_sociales = []
    
    return {
        'config': config,
        'enlaces_externos': enlaces_externos,
        'comunicados_home': comunicados_home,
        'comunicados_popup': comunicados_popup,
        'noticias_recientes': noticias_recientes,
        'redes_sociales': redes_sociales,
    } 