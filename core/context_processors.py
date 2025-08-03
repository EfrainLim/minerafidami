from .models import RedSocial, ConfiguracionGeneral, HeroSection
import random


def redes_sociales(request):
    """Context processor para incluir redes sociales en todas las plantillas"""
    try:
        redes = RedSocial.objects.filter(activo=True).order_by('orden')
    except:
        redes = []
    
    return {
        'redes_sociales': redes
    }


def configuracion_general(request):
    """Context processor para incluir la configuración general en todas las plantillas"""
    try:
        config = ConfiguracionGeneral.objects.first()
    except:
        config = None
    
    return {
        'config': config
    }


def hero_section_context(request):
    """Context processor para incluir el hero section en todas las plantillas"""
    try:
        # Obtener todos los hero sections activos ordenados
        heroes_activos = list(HeroSection.objects.filter(activo=True).order_by('orden'))
        
        if heroes_activos:
            # Si hay múltiples, seleccionar uno aleatoriamente
            if len(heroes_activos) > 1:
                # Selección aleatoria simple
                hero = random.choice(heroes_activos)
            else:
                # Si solo hay uno, usarlo directamente
                hero = heroes_activos[0]
        else:
            hero = None
            
    except:
        hero = None
    
    return {
        'hero_section': hero
    } 