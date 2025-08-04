from django.core.management.base import BaseCommand
from django.contrib.sitemaps.views import sitemap
from django.test import RequestFactory
from django.conf import settings
from core.sitemaps import StaticViewSitemap, ServicioSitemap, ProyectoSitemap, NoticiaSitemap
import os


class Command(BaseCommand):
    help = 'Genera sitemap.xml estáticamente'

    def handle(self, *args, **options):
        self.stdout.write('Generando sitemap.xml...')
        
        # Crear request factory
        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        request.META['HTTP_HOST'] = 'minerafidami.com.pe'
        request.META['SERVER_NAME'] = 'minerafidami.com.pe'
        request.META['SERVER_PORT'] = '80'
        request.META['wsgi.url_scheme'] = 'https'
        
        # Configurar sitemaps
        sitemaps = {
            'static': StaticViewSitemap,
            'servicios': ServicioSitemap,
            'proyectos': ProyectoSitemap,
            'noticias': NoticiaSitemap,
        }
        
        try:
            # Generar sitemap
            response = sitemap(request, sitemaps=sitemaps)
            
            # Crear directorio static si no existe
            static_dir = os.path.join(settings.BASE_DIR, 'static')
            os.makedirs(static_dir, exist_ok=True)
            
            # Guardar sitemap
            sitemap_path = os.path.join(static_dir, 'sitemap.xml')
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(response.content.decode('utf-8'))
            
            self.stdout.write(
                self.style.SUCCESS(f'Sitemap generado exitosamente en {sitemap_path}')
            )
            self.stdout.write(f'Tamaño: {len(response.content)} bytes')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error generando sitemap: {e}')
            ) 