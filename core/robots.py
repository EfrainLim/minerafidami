from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.urls import path


@cache_page(60 * 60 * 24)  # Cache por 24 horas
def robots_txt(request):
    """Genera robots.txt dinámicamente"""
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "# Sitemap",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
        "",
        "# Disallow admin and private areas",
        "Disallow: /admin/",
        "Disallow: /static/admin/",
        "Disallow: /media/admin/",
        "",
        "# Allow important pages",
        "Allow: /servicios/",
        "Allow: /proyectos/",
        "Allow: /blog/",
        "Allow: /carreras/",
        "Allow: /contacto/",
        "",
        "# Crawl delay (opcional)",
        "Crawl-delay: 1",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


urlpatterns = [
    path('', robots_txt, name='robots_txt'),
] 