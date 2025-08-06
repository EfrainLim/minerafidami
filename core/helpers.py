from django.utils import timezone
from django.db.models import Q


def safe_get_queryset(queryset, default=None):
    """
    Helper para obtener querysets de forma segura.
    
    Args:
        queryset: QuerySet a ejecutar
        default: Valor por defecto si hay error
        
    Returns:
        QuerySet o valor por defecto
    """
    try:
        return queryset
    except Exception:
        return default or []


def get_comunicados_activos(mostrar_en, limit=5):
    """
    Helper para obtener comunicados activos.
    
    Args:
        mostrar_en (str): Campo a filtrar (mostrar_en_home, mostrar_en_popup)
        limit (int): Límite de resultados
        
    Returns:
        QuerySet de comunicados activos
    """
    from comunicados.models import Comunicado
    
    return Comunicado.objects.filter(
        **{mostrar_en: True},
        estado='publicado',
        activo=True
    ).filter(
        Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
    ).filter(
        Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
    ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:limit]


def get_hero_section_with_rotation():
    """
    Helper para obtener hero section con rotación automática.
    
    Returns:
        HeroSection o None
    """
    from core.models import HeroSection
    import time
    
    heroes_activos = list(HeroSection.objects.filter(activo=True).order_by('orden'))
    if not heroes_activos:
        return None
    
    current_time = int(time.time())
    rotation_interval = 30
    current_index = (current_time // rotation_interval) % len(heroes_activos)
    return heroes_activos[current_index]


def get_destacados(model_class, limit=6, **filters):
    """
    Helper para obtener elementos destacados de cualquier modelo.
    
    Args:
        model_class: Clase del modelo
        limit (int): Límite de resultados
        **filters: Filtros adicionales
        
    Returns:
        QuerySet de elementos destacados
    """
    try:
        return model_class.objects.filter(
            estado='activo',
            destacado=True,
            **filters
        ).order_by('orden')[:limit]
    except Exception:
        return []


def get_recientes(model_class, limit=3, **filters):
    """
    Helper para obtener elementos recientes de cualquier modelo.
    
    Args:
        model_class: Clase del modelo
        limit (int): Límite de resultados
        **filters: Filtros adicionales
        
    Returns:
        QuerySet de elementos recientes
    """
    try:
        return model_class.objects.filter(
            estado='publicado',
            **filters
        ).order_by('-fecha_publicacion')[:limit]
    except Exception:
        return [] 