from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Servicio, CategoriaServicio
from core.models import ConfiguracionGeneral


class ServicioListView(ListView):
    """Vista para listar todos los servicios"""
    model = Servicio
    template_name = 'servicios/servicio_list.html'
    context_object_name = 'servicios'
    
    def get_queryset(self):
        return Servicio.objects.filter(estado='activo').order_by('orden')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        categorias = CategoriaServicio.objects.filter(estado='activo').order_by('orden')
        
        context.update({
            'config': config,
            'categorias': categorias,
        })
        return context


class ServicioDetailView(DetailView):
    """Vista para detalle de servicio"""
    model = Servicio
    template_name = 'servicios/servicio_detail.html'
    context_object_name = 'servicio'
    
    def get_queryset(self):
        return Servicio.objects.filter(estado='activo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener servicios relacionados
        servicios_relacionados = Servicio.objects.filter(
            estado='activo'
        ).exclude(id=self.object.id).order_by('orden')[:3]
        
        context.update({
            'config': config,
            'servicios_relacionados': servicios_relacionados,
        })
        return context


class CategoriaServicioView(DetailView):
    """Vista para servicios por categoría"""
    model = CategoriaServicio
    template_name = 'servicios/categoria_servicio.html'
    context_object_name = 'categoria'
    
    def get_queryset(self):
        return CategoriaServicio.objects.filter(estado='activo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener servicios de esta categoría
        servicios = Servicio.objects.filter(
            estado='activo'
        ).order_by('orden')
        
        context.update({
            'config': config,
            'servicios': servicios,
        })
        return context
