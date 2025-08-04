#!/usr/bin/env python
"""
Script para verificar y solucionar problemas del sitemap
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minerafidami.settings')
django.setup()

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.http import HttpRequest
from django.test import RequestFactory
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, ServicioSitemap, ProyectoSitemap, NoticiaSitemap
from servicios.models import Servicio
from proyectos.models import Proyecto
from blog.models import NoticiaBlog

def verificar_sitemaps():
    """Verificar que todos los sitemaps funcionan correctamente"""
    print("🔍 Verificando sitemaps...")
    
    # Verificar modelos
    print("\n📊 Datos disponibles:")
    print(f"Servicios activos: {Servicio.objects.filter(estado='activo').count()}")
    print(f"Proyectos activos: {Proyecto.objects.filter(estado='activo').count()}")
    print(f"Noticias publicadas: {NoticiaBlog.objects.filter(estado='publicado').count()}")
    
    # Verificar URLs estáticas
    print("\n🌐 URLs estáticas:")
    static_sitemap = StaticViewSitemap()
    for item in static_sitemap.items():
        try:
            url = static_sitemap.location(item)
            print(f"✅ {item}: {url}")
        except Exception as e:
            print(f"❌ {item}: Error - {e}")
    
    # Verificar sitemaps dinámicos
    print("\n📄 Sitemaps dinámicos:")
    
    # Servicios
    try:
        servicios = ServicioSitemap().items()
        print(f"✅ Servicios: {servicios.count()} elementos")
    except Exception as e:
        print(f"❌ Servicios: Error - {e}")
    
    # Proyectos
    try:
        proyectos = ProyectoSitemap().items()
        print(f"✅ Proyectos: {proyectos.count()} elementos")
    except Exception as e:
        print(f"❌ Proyectos: Error - {e}")
    
    # Noticias
    try:
        noticias = NoticiaSitemap().items()
        print(f"✅ Noticias: {noticias.count()} elementos")
    except Exception as e:
        print(f"❌ Noticias: Error - {e}")

def generar_sitemap_manual():
    """Generar sitemap manualmente para verificar"""
    print("\n🔧 Generando sitemap manualmente...")
    
    # Crear request factory
    factory = RequestFactory()
    request = factory.get('/sitemap.xml')
    request.META['HTTP_HOST'] = 'minerafidami.com.pe'
    request.META['SERVER_NAME'] = 'minerafidami.com.pe'
    request.META['SERVER_PORT'] = '80'
    request.META['wsgi.url_scheme'] = 'http'
    
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
        print(f"✅ Sitemap generado correctamente")
        print(f"📄 Tamaño: {len(response.content)} bytes")
        print(f"🔗 URL: {request.build_absolute_uri('/sitemap.xml')}")
        
        # Guardar sitemap para verificar
        with open('/tmp/sitemap_test.xml', 'w') as f:
            f.write(response.content.decode('utf-8'))
        print("💾 Sitemap guardado en /tmp/sitemap_test.xml")
        
    except Exception as e:
        print(f"❌ Error generando sitemap: {e}")
        import traceback
        traceback.print_exc()

def verificar_robots():
    """Verificar robots.txt"""
    print("\n🤖 Verificando robots.txt...")
    
    from core.robots import robots_txt
    from django.test import RequestFactory
    
    factory = RequestFactory()
    request = factory.get('/robots.txt')
    request.META['HTTP_HOST'] = 'minerafidami.com.pe'
    
    try:
        response = robots_txt(request)
        print(f"✅ Robots.txt generado correctamente")
        print(f"📄 Tamaño: {len(response.content)} bytes")
        print(f"🔗 Sitemap URL en robots.txt: {request.build_absolute_uri('/sitemap.xml')}")
        
        # Guardar robots.txt para verificar
        with open('/tmp/robots_test.txt', 'w') as f:
            f.write(response.content.decode('utf-8'))
        print("💾 Robots.txt guardado en /tmp/robots_test.txt")
        
    except Exception as e:
        print(f"❌ Error generando robots.txt: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("🚀 Verificando configuración de SEO...")
    verificar_sitemaps()
    generar_sitemap_manual()
    verificar_robots()
    print("\n✅ Verificación completada") 