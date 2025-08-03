from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import NoticiaBlog, CategoriaBlog
from core.models import ConfiguracionGeneral


class BlogListView(ListView):
    """Vista para listar todas las noticias y artículos"""
    model = NoticiaBlog
    template_name = 'blog/blog_list.html'
    context_object_name = 'noticias'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = NoticiaBlog.objects.filter(estado='publicado').order_by('-fecha_publicacion')
        
        # Filtrar por categoría si se especifica
        categoria_slug = self.request.GET.get('categoria')
        if categoria_slug:
            try:
                categoria = CategoriaBlog.objects.get(slug=categoria_slug, estado='activo')
                queryset = queryset.filter(categoria=categoria)
            except CategoriaBlog.DoesNotExist:
                pass
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        categorias = CategoriaBlog.objects.filter(estado='activo').order_by('orden')
        
        # Obtener categoría actual
        categoria_actual = None
        categoria_slug = self.request.GET.get('categoria')
        if categoria_slug:
            try:
                categoria_actual = CategoriaBlog.objects.get(slug=categoria_slug, estado='activo')
            except CategoriaBlog.DoesNotExist:
                pass
        
        context.update({
            'config': config,
            'categorias': categorias,
            'categoria_actual': categoria_actual,
        })
        return context


class NoticiaDetailView(DetailView):
    """Vista para detalle de noticia"""
    model = NoticiaBlog
    template_name = 'blog/noticia_detail.html'
    context_object_name = 'noticia'
    
    def get_queryset(self):
        return NoticiaBlog.objects.filter(estado='publicado')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Incrementar contador de vistas
        self.object.vistas += 1
        self.object.save()
        
        # Obtener noticias relacionadas
        noticias_relacionadas = NoticiaBlog.objects.filter(
            estado='publicado',
            categoria=self.object.categoria
        ).exclude(id=self.object.id).order_by('-fecha_publicacion')[:3]
        
        # Obtener noticias destacadas
        noticias_destacadas = NoticiaBlog.objects.filter(
            estado='publicado',
            destacado=True
        ).exclude(id=self.object.id).order_by('-fecha_publicacion')[:3]
        
        context.update({
            'config': config,
            'noticias_relacionadas': noticias_relacionadas,
            'noticias_destacadas': noticias_destacadas,
        })
        return context


class CategoriaBlogView(DetailView):
    """Vista para noticias por categoría"""
    model = CategoriaBlog
    template_name = 'blog/categoria_blog.html'
    context_object_name = 'categoria'
    
    def get_queryset(self):
        return CategoriaBlog.objects.filter(estado='activo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener noticias de esta categoría
        noticias = NoticiaBlog.objects.filter(
            estado='publicado',
            categoria=self.object
        ).order_by('-fecha_publicacion')
        
        context.update({
            'config': config,
            'noticias': noticias,
        })
        return context
