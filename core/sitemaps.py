from django.contrib.sitemaps import Sitemap
from servicios.models import Servicio
from proyectos.models import Proyecto
from blog.models import NoticiaBlog
from django.utils import timezone


class StaticViewSitemap(Sitemap):
    """Sitemap para páginas estáticas"""
    priority = 1.0
    changefreq = 'weekly'
    lastmod = timezone.now()

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
        # URLs directas sin usar reverse()
        urls = {
            'home': '/',
            'sobre_nosotros': '/sobre-nosotros/',
            'servicios': '/servicios/',
            'proyectos': '/proyectos/',
            'innovacion': '/innovacion/',
            'responsabilidad_social': '/responsabilidad-social/',
            'blog': '/blog/',
            'carreras': '/carreras/',
            'contacto': '/contacto/',
        }
        return urls.get(item, f"/{item}/")


class ServicioSitemap(Sitemap):
    """Sitemap para servicios"""
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        try:
            return Servicio.objects.filter(estado='activo')
        except Exception as e:
            print(f"Error obteniendo servicios: {e}")
            return []

    def location(self, obj):
        return f"/servicios/{obj.slug}/"

    def lastmod(self, obj):
        try:
            return obj.updated_at
        except:
            return None


class ProyectoSitemap(Sitemap):
    """Sitemap para proyectos"""
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        try:
            return Proyecto.objects.filter(estado='activo')
        except Exception as e:
            print(f"Error obteniendo proyectos: {e}")
            return []

    def location(self, obj):
        return f"/proyectos/{obj.slug}/"

    def lastmod(self, obj):
        try:
            return obj.updated_at
        except:
            return None


class NoticiaSitemap(Sitemap):
    """Sitemap para noticias del blog"""
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        try:
            return NoticiaBlog.objects.filter(estado='publicado')
        except Exception as e:
            print(f"Error obteniendo noticias: {e}")
            return []

    def location(self, obj):
        return f"/blog/{obj.slug}/"

    def lastmod(self, obj):
        try:
            return obj.updated_at
        except:
            return None 