from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.utils import timezone
from .models import Comunicado, CategoriaComunicado


class ComunicadoListView(ListView):
    """Vista para listar todos los comunicados"""
    model = Comunicado
    template_name = 'comunicados/comunicado_list.html'
    context_object_name = 'comunicados'
    paginate_by = 12
    
    def get_queryset(self):
        """Obtener comunicados activos y publicados"""
        queryset = Comunicado.objects.filter(
            estado='publicado',
            activo=True
        ).filter(
            Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
        ).filter(
            Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
        )
        
        # Filtro por categoría
        categoria_slug = self.request.GET.get('categoria')
        if categoria_slug:
            queryset = queryset.filter(categoria__slug=categoria_slug)
        
        # Filtro por tipo
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        
        # Filtro por prioridad
        prioridad = self.request.GET.get('prioridad')
        if prioridad:
            queryset = queryset.filter(prioridad=prioridad)
        
        # Búsqueda
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(titulo__icontains=q) |
                Q(resumen__icontains=q) |
                Q(contenido__icontains=q)
            )
        
        return queryset.order_by('-fecha_publicacion', '-prioridad', 'orden')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Categorías para filtros
        context['categorias'] = CategoriaComunicado.objects.filter(activo=True).order_by('orden')
        
        # Tipos para filtros
        context['tipos'] = Comunicado.TIPO_CHOICES
        
        # Prioridades para filtros
        context['prioridades'] = Comunicado.PRIORIDAD_CHOICES
        
        # Comunicados destacados
        context['comunicados_destacados'] = self.get_queryset().filter(destacado=True)[:3]
        
        return context


class ComunicadoDetailView(DetailView):
    """Vista para mostrar un comunicado específico"""
    model = Comunicado
    template_name = 'comunicados/comunicado_detail.html'
    context_object_name = 'comunicado'
    
    def get_queryset(self):
        """Obtener comunicado activo y publicado"""
        return Comunicado.objects.filter(
            estado='publicado',
            activo=True
        ).filter(
            Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
        ).filter(
            Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
        )
    
    def get_object(self, queryset=None):
        """Obtener objeto por slug y registrar vista"""
        obj = super().get_object(queryset)
        # Incrementar contador de vistas
        obj.incrementar_vista()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Comunicados relacionados (misma categoría)
        comunicado = self.get_object()
        if comunicado.categoria:
            context['comunicados_relacionados'] = Comunicado.objects.filter(
                categoria=comunicado.categoria,
                estado='publicado',
                activo=True
            ).exclude(id=comunicado.id)[:3]
        else:
            context['comunicados_relacionados'] = []
        
        # Comunicados recientes
        context['comunicados_recientes'] = Comunicado.objects.filter(
            estado='publicado',
            activo=True
        ).exclude(id=comunicado.id).order_by('-fecha_publicacion')[:5]
        
        # Nombre del archivo adjunto (si existe)
        if comunicado.archivo_adjunto:
            import os
            context['nombre_archivo'] = os.path.basename(comunicado.archivo_adjunto.name)
        else:
            context['nombre_archivo'] = None
        
        return context


def comunicados_home(request):
    """Vista para comunicados en la página principal"""
    comunicados_home = Comunicado.objects.filter(
        mostrar_en_home=True,
        estado='publicado',
        activo=True
    ).filter(
        Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
    ).filter(
        Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
    ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:5]
    
    return {
        'comunicados_home': comunicados_home
    }


def comunicados_popup(request):
    """Vista para comunicados en popup"""
    comunicados_popup = Comunicado.objects.filter(
        mostrar_en_popup=True,
        estado='publicado',
        activo=True
    ).filter(
        Q(fecha_publicacion__lte=timezone.now()) | Q(fecha_publicacion__isnull=True)
    ).filter(
        Q(fecha_expiracion__gte=timezone.now()) | Q(fecha_expiracion__isnull=True)
    ).order_by('-prioridad', '-fecha_publicacion', 'orden')[:3]
    
    return {
        'comunicados_popup': comunicados_popup
    }
