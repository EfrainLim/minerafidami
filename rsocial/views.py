from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import ProgramaSocial, Alianza, ImpactoAmbiental, ReporteSostenibilidad


class ResponsabilidadSocialHomeView(TemplateView):
    """Vista principal de la sección de responsabilidad social"""
    template_name = 'rsocial/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programas_destacados'] = ProgramaSocial.objects.filter(
            estado='activo', destacado=True
        ).order_by('orden')[:6]
        context['alianzas_destacadas'] = Alianza.objects.filter(
            estado='activa', destacado=True
        ).order_by('orden')[:4]
        context['impactos_destacados'] = ImpactoAmbiental.objects.filter(
            estado='activo', destacado=True
        ).order_by('orden')[:3]
        context['ultimo_reporte'] = ReporteSostenibilidad.objects.filter(
            estado='publicado'
        ).order_by('-año').first()
        return context


class ProgramaSocialListView(ListView):
    """Lista de programas sociales"""
    model = ProgramaSocial
    template_name = 'rsocial/programa_list.html'
    context_object_name = 'programas'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = ProgramaSocial.objects.filter(estado='activo')
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        return queryset.order_by('-created_at', '-orden', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.db.models import Count
        context['categorias'] = ProgramaSocial.objects.filter(
            estado='activo'
        ).values('categoria').annotate(
            count=Count('categoria')
        ).values_list('categoria', flat=True).order_by('categoria')
        return context


class ProgramaSocialDetailView(DetailView):
    """Detalle de un programa social"""
    model = ProgramaSocial
    template_name = 'rsocial/programa_detail.html'
    context_object_name = 'programa'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        programa = self.get_object()
        context['programas_relacionados'] = ProgramaSocial.objects.filter(
            estado='activo',
            categoria=programa.categoria
        ).exclude(id=programa.id)[:3]
        return context


class AlianzaListView(ListView):
    """Lista de alianzas estratégicas"""
    model = Alianza
    template_name = 'rsocial/alianza_list.html'
    context_object_name = 'alianzas'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Alianza.objects.filter(estado='activa')
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo_alianza=tipo)
        return queryset.order_by('-created_at', '-orden', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.db.models import Count
        context['tipos_alianza'] = Alianza.objects.filter(
            estado='activa'
        ).values('tipo_alianza').annotate(
            count=Count('tipo_alianza')
        ).values_list('tipo_alianza', flat=True).order_by('tipo_alianza')
        return context


class AlianzaDetailView(DetailView):
    """Detalle de una alianza"""
    model = Alianza
    template_name = 'rsocial/alianza_detail.html'
    context_object_name = 'alianza'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alianza = self.get_object()
        context['alianzas_relacionadas'] = Alianza.objects.filter(
            estado='activa',
            tipo_alianza=alianza.tipo_alianza
        ).exclude(id=alianza.id)[:3]
        return context


class ImpactoAmbientalListView(ListView):
    """Lista de impactos ambientales"""
    model = ImpactoAmbiental
    template_name = 'rsocial/impacto_list.html'
    context_object_name = 'impactos'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = ImpactoAmbiental.objects.filter(estado='activo')
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        return queryset.order_by('-created_at', '-orden', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.db.models import Count
        context['categorias'] = ImpactoAmbiental.objects.filter(
            estado='activo'
        ).values('categoria').annotate(
            count=Count('categoria')
        ).values_list('categoria', flat=True).order_by('categoria')
        return context


class ImpactoAmbientalDetailView(DetailView):
    """Detalle de un impacto ambiental"""
    model = ImpactoAmbiental
    template_name = 'rsocial/impacto_detail.html'
    context_object_name = 'impacto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        impacto = self.get_object()
        context['impactos_relacionados'] = ImpactoAmbiental.objects.filter(
            estado='activo',
            categoria=impacto.categoria
        ).exclude(id=impacto.id)[:3]
        return context


class ReporteSostenibilidadListView(ListView):
    """Lista de reportes de sostenibilidad"""
    model = ReporteSostenibilidad
    template_name = 'rsocial/reporte_list.html'
    context_object_name = 'reportes'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = ReporteSostenibilidad.objects.filter(estado='publicado')
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo_reporte=tipo)
        return queryset.order_by('-año', 'orden')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.db.models import Count
        context['tipos_reporte'] = ReporteSostenibilidad.objects.filter(
            estado='publicado'
        ).values('tipo_reporte').annotate(
            count=Count('tipo_reporte')
        ).values_list('tipo_reporte', flat=True).order_by('tipo_reporte')
        return context


class ReporteSostenibilidadDetailView(DetailView):
    """Detalle de un reporte de sostenibilidad"""
    model = ReporteSostenibilidad
    template_name = 'rsocial/reporte_detail.html'
    context_object_name = 'reporte'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reporte = self.get_object()
        context['reportes_relacionados'] = ReporteSostenibilidad.objects.filter(
            estado='publicado',
            tipo_reporte=reporte.tipo_reporte
        ).exclude(id=reporte.id)[:3]
        return context


class ResponsabilidadSocialSearchView(ListView):
    """Búsqueda en responsabilidad social"""
    template_name = 'rsocial/search.html'
    context_object_name = 'resultados'
    paginate_by = 12
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            return []
        
        # Buscar en programas sociales
        programas = ProgramaSocial.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion_corta__icontains=query) |
            Q(descripcion_larga__icontains=query),
            estado='activo'
        )
        
        # Buscar en alianzas
        alianzas = Alianza.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query),
            estado='activa'
        )
        
        # Buscar en impactos ambientales
        impactos = ImpactoAmbiental.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion_corta__icontains=query) |
            Q(descripcion_larga__icontains=query),
            estado='activo'
        )
        
        # Buscar en reportes
        reportes = ReporteSostenibilidad.objects.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query),
            estado='publicado'
        )
        
        # Combinar resultados
        resultados = list(programas) + list(alianzas) + list(impactos) + list(reportes)
        return resultados
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
