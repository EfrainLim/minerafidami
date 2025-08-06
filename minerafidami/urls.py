"""
URL configuration for minerafidami project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, ServicioSitemap, ProyectoSitemap, NoticiaSitemap

# Configuración simple del admin
admin.site.site_header = "Minera Fidami S.A."
admin.site.site_title = "Minera Fidami S.A."
admin.site.index_title = "Panel de Administración - Minera Fidami S.A."

# Sitemaps
sitemaps = {
    'static': StaticViewSitemap,
    'servicios': ServicioSitemap,
    'proyectos': ProyectoSitemap,
    'noticias': NoticiaSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('servicios/', include('servicios.urls')),
    path('proyectos/', include('proyectos.urls')),
    path('innovacion/', include('innovacion.urls')),
    path('responsabilidad-social/', include('rsocial.urls')),
    path('blog/', include('blog.urls')),
    path('carreras/', include('carreras.urls')),
    path('contacto/', include('contacto.urls')),
    path('comunicados/', include('comunicados.urls')),
    
    # SEO URLs
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('core.robots')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
