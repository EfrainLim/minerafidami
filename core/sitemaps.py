from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from servicios.models import Servicio
from proyectos.models import Proyecto
from blog.models import NoticiaBlog


class StaticViewSitemap(Sitemap):
    """Sitemap para páginas estáticas"""
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return [
            'home',
            'sobre_nosotros',
            'servicios',
            'proyectos',
            'innovacion',
            'responsabilidad_social',
            'blog',
            'carreras',
            'contacto',
        ]

    def location(self, item):
        if item == 'home':
            return reverse('home')
        elif item == 'sobre_nosotros':
            return reverse('sobre_nosotros')
        elif item == 'servicios':
            return reverse('servicios:servicio_list')
        elif item == 'proyectos':
            return reverse('proyectos:proyecto_list')
        elif item == 'innovacion':
            return reverse('innovacion:home')
        elif item == 'responsabilidad_social':
            return reverse('rsocial:home')
        elif item == 'blog':
            return reverse('blog:blog_list')
        elif item == 'carreras':
            return reverse('carreras:vacante_list')
        elif item == 'contacto':
            return reverse('contacto:contacto')


class ServicioSitemap(Sitemap):
    """Sitemap para servicios"""
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Servicio.objects.filter(estado='activo')

    def lastmod(self, obj):
        return obj.updated_at


class ProyectoSitemap(Sitemap):
    """Sitemap para proyectos"""
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Proyecto.objects.filter(estado='activo')

    def lastmod(self, obj):
        return obj.updated_at


class NoticiaSitemap(Sitemap):
    """Sitemap para noticias del blog"""
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return NoticiaBlog.objects.filter(estado='publicado')

    def lastmod(self, obj):
        return obj.updated_at 