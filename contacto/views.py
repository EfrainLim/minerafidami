from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Contacto, Newsletter
from core.models import ConfiguracionGeneral


def contacto_view(request):
    """Vista para página de contacto"""
    if request.method == 'POST':
        # Procesar formulario de contacto
        contacto = Contacto.objects.create(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            empresa=request.POST.get('empresa'),
            cargo=request.POST.get('cargo'),
            asunto=request.POST.get('asunto'),
            mensaje=request.POST.get('mensaje'),
            tipo_consulta=request.POST.get('tipo_consulta', 'general'),
        )
        
        messages.success(request, 'Tu mensaje ha sido enviado exitosamente. Te responderemos pronto.')
        return HttpResponseRedirect(reverse('contacto'))
    
    try:
        config = ConfiguracionGeneral.objects.first()
    except:
        config = None
    
    context = {
        'config': config,
    }
    
    return render(request, 'contacto/contacto.html', context)


def suscribir_newsletter(request):
    """Vista para suscribirse al newsletter"""
    if request.method == 'POST':
        email = request.POST.get('email')
        nombre = request.POST.get('nombre', '')
        empresa = request.POST.get('empresa', '')
        cargo = request.POST.get('cargo', '')
        
        if email:
            # Verificar si ya existe
            newsletter, created = Newsletter.objects.get_or_create(
                email=email,
                defaults={
                    'nombre': nombre,
                    'empresa': empresa,
                    'cargo': cargo,
                }
            )
            
            if created:
                messages.success(request, 'Te has suscrito exitosamente a nuestro newsletter.')
            else:
                messages.info(request, 'Ya estás suscrito a nuestro newsletter.')
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    return HttpResponseRedirect('/')
