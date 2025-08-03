from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Tecnologia, ProyectoInnovacion, Patente


class InnovacionHomeView(TemplateView):
    """Vista principal de la sección de innovación"""
    template_name = 'innovacion/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tecnologias_destacadas'] = Tecnologia.objects.filter(
            estado='activo', destacado=True
        ).order_by('orden')[:6]
        context['proyectos_destacados'] = ProyectoInnovacion.objects.filter(
            estado='activo', destacado=True
        ).order_by('orden')[:4]
        context['patentes_destacadas'] = Patente.objects.filter(
            estado='vigente', destacado=True
        ).order_by('orden')[:3]
        return context


class TecnologiaListView(ListView):
    """Lista de tecnologías innovadoras"""
    model = Tecnologia
    template_name = 'innovacion/tecnologia_list.html'
    context_object_name = 'tecnologias'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Tecnologia.objects.filter(estado='activo')
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        return queryset.order_by('orden', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Tecnologia.objects.filter(
            estado='activo'
        ).values_list('categoria', flat=True).distinct()
        return context


class TecnologiaDetailView(DetailView):
    """Detalle de una tecnología"""
    model = Tecnologia
    template_name = 'innovacion/tecnologia_detail.html'
    context_object_name = 'tecnologia'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Incrementar vistas si es necesario
        tecnologia = self.get_object()
        context['tecnologias_relacionadas'] = Tecnologia.objects.filter(
            estado='activo',
            categoria=tecnologia.categoria
        ).exclude(id=tecnologia.id)[:3]
        return context


class ProyectoInnovacionListView(ListView):
    """Lista de proyectos de innovación"""
    model = ProyectoInnovacion
    template_name = 'innovacion/proyecto_list.html'
    context_object_name = 'proyectos'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = ProyectoInnovacion.objects.filter(estado='activo')
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo_proyecto=tipo)
        return queryset.order_by('orden', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener tipos únicos de proyectos activos usando annotate para evitar duplicados
        from django.db.models import Count
        context['tipos_proyecto'] = ProyectoInnovacion.objects.filter(
            estado='activo'
        ).values('tipo_proyecto').annotate(
            count=Count('tipo_proyecto')
        ).values_list('tipo_proyecto', flat=True).order_by('tipo_proyecto')
        return context


class ProyectoInnovacionDetailView(DetailView):
    """Detalle de un proyecto de innovación"""
    model = ProyectoInnovacion
    template_name = 'innovacion/proyecto_detail.html'
    context_object_name = 'proyecto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proyecto = self.get_object()
        context['proyectos_relacionados'] = ProyectoInnovacion.objects.filter(
            estado='activo',
            tipo_proyecto=proyecto.tipo_proyecto
        ).exclude(id=proyecto.id)[:3]
        return context


class PatenteListView(ListView):
    """Lista de patentes y propiedad intelectual"""
    model = Patente
    template_name = 'innovacion/patente_list.html'
    context_object_name = 'patentes'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Patente.objects.filter(estado__in=['vigente', 'aprobada'])
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        return queryset.order_by('orden', 'titulo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener tipos únicos de patentes activas usando annotate para evitar duplicados
        from django.db.models import Count
        context['tipos_patente'] = Patente.objects.filter(
            estado__in=['vigente', 'aprobada']
        ).values('tipo').annotate(
            count=Count('tipo')
        ).values_list('tipo', flat=True).order_by('tipo')
        return context


class PatenteDetailView(DetailView):
    """Detalle de una patente"""
    model = Patente
    template_name = 'innovacion/patente_detail.html'
    context_object_name = 'patente'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patente = self.get_object()
        context['patentes_relacionadas'] = Patente.objects.filter(
            estado__in=['vigente', 'aprobada'],
            tipo=patente.tipo
        ).exclude(id=patente.id)[:3]
        return context


class InnovacionSearchView(ListView):
    """Búsqueda en innovación"""
    template_name = 'innovacion/search.html'
    context_object_name = 'resultados'
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            return []
        
        # Buscar en tecnologías
        tecnologias = Tecnologia.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion_corta__icontains=query) |
            Q(descripcion_larga__icontains=query),
            estado='activo'
        )
        
        # Buscar en proyectos
        proyectos = ProyectoInnovacion.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion_corta__icontains=query) |
            Q(descripcion_larga__icontains=query),
            estado='activo'
        )
        
        # Buscar en patentes
        patentes = Patente.objects.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query),
            estado__in=['vigente', 'aprobada']
        )
        
        # Combinar resultados
        resultados = list(tecnologias) + list(proyectos) + list(patentes)
        return resultados
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
