from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Vacante, Postulacion
from core.models import ConfiguracionGeneral


class VacanteListView(ListView):
    """Vista para listar todas las vacantes"""
    model = Vacante
    template_name = 'carreras/vacante_list.html'
    context_object_name = 'vacantes'
    
    def get_queryset(self):
        return Vacante.objects.filter(estado='abierta').order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Filtrar por departamento si se especifica
        departamento = self.request.GET.get('departamento')
        if departamento:
            context['vacantes'] = Vacante.objects.filter(
                estado='abierta',
                departamento=departamento
            ).order_by('-created_at')
        
        # Obtener departamentos únicos
        departamentos = Vacante.objects.filter(
            estado='abierta'
        ).values_list('departamento', flat=True).distinct()
        
        context.update({
            'config': config,
            'departamentos': departamentos,
            'departamento_actual': departamento,
        })
        return context


class VacanteDetailView(DetailView):
    """Vista para detalle de vacante"""
    model = Vacante
    template_name = 'carreras/vacante_detail.html'
    context_object_name = 'vacante'
    
    def get_queryset(self):
        return Vacante.objects.filter(estado='abierta')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Incrementar contador de vistas
        self.object.vistas += 1
        self.object.save()
        
        # Obtener vacantes relacionadas
        vacantes_relacionadas = Vacante.objects.filter(
            estado='abierta',
            departamento=self.object.departamento
        ).exclude(id=self.object.id).order_by('-created_at')[:3]
        
        context.update({
            'config': config,
            'vacantes_relacionadas': vacantes_relacionadas,
        })
        return context


def postular_vacante(request, slug):
    """Vista para postular a una vacante"""
    if request.method == 'POST':
        vacante = get_object_or_404(Vacante, slug=slug, estado='abierta')
        
        # Crear postulación
        postulacion = Postulacion.objects.create(
            vacante=vacante,
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            nacionalidad=request.POST.get('nacionalidad'),
            experiencia_anos=request.POST.get('experiencia_anos'),
            educacion=request.POST.get('educacion'),
            cv_url=request.POST.get('cv_url'),
            carta_motivacion=request.POST.get('carta_motivacion'),
            referencias=request.POST.get('referencias'),
        )
        
        # Incrementar contador de postulaciones
        vacante.postulaciones += 1
        vacante.save()
        
        messages.success(request, 'Tu postulación ha sido enviada exitosamente.')
        return HttpResponseRedirect(reverse('vacante_detail', kwargs={'slug': slug}))
    
    return HttpResponseRedirect(reverse('vacante_detail', kwargs={'slug': slug}))
