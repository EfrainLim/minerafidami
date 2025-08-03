from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Proyecto, CategoriaProyecto
from core.models import ConfiguracionGeneral


class ProyectoListView(ListView):
    """Vista para listar todos los proyectos"""
    model = Proyecto
    template_name = 'proyectos/proyecto_list.html'
    context_object_name = 'proyectos'
    paginate_by = 9  # Mostrar 9 proyectos por página (3x3 grid)
    
    def get_queryset(self):
        queryset = Proyecto.objects.filter(estado='activo').order_by('-fecha_inicio')
        
        # Filtrar por categoría si se especifica
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria__slug=categoria)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener categorías activas
        categorias = CategoriaProyecto.objects.filter(estado='activo').order_by('orden')
        
        context.update({
            'config': config,
            'categorias': categorias,
            'categoria_actual': self.request.GET.get('categoria'),
        })
        return context


class ProyectoDetailView(DetailView):
    """Vista para detalle de proyecto"""
    model = Proyecto
    template_name = 'proyectos/proyecto_detail.html'
    context_object_name = 'proyecto'
    
    def get_queryset(self):
        return Proyecto.objects.filter(estado='activo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener proyectos relacionados por categoría
        proyectos_relacionados = Proyecto.objects.filter(
            estado='activo',
            categoria=self.object.categoria
        ).exclude(id=self.object.id).order_by('-fecha_inicio')[:3]
        
        context.update({
            'config': config,
            'proyectos_relacionados': proyectos_relacionados,
        })
        return context


class CategoriaProyectoView(DetailView):
    """Vista para proyectos por categoría"""
    model = CategoriaProyecto
    template_name = 'proyectos/categoria_proyecto.html'
    context_object_name = 'categoria'
    
    def get_queryset(self):
        return CategoriaProyecto.objects.filter(estado='activo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener proyectos de esta categoría
        proyectos = Proyecto.objects.filter(
            estado='activo'
        ).order_by('-fecha_inicio')
        
        context.update({
            'config': config,
            'proyectos': proyectos,
        })
        return context
