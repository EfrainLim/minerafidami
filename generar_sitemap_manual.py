#!/usr/bin/env python
"""
Script para generar sitemap.xml manualmente
"""
import os
from datetime import datetime

def generar_sitemap_manual():
    """Generar sitemap.xml manualmente"""
    
    # URLs estáticas
    urls_estaticas = [
        {'url': 'https://minerafidami.com.pe/', 'priority': '1.0', 'changefreq': 'weekly'},
        {'url': 'https://minerafidami.com.pe/sobre-nosotros/', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': 'https://minerafidami.com.pe/servicios/', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': 'https://minerafidami.com.pe/proyectos/', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': 'https://minerafidami.com.pe/innovacion/', 'priority': '0.8', 'changefreq': 'weekly'},
        {'url': 'https://minerafidami.com.pe/responsabilidad-social/', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': 'https://minerafidami.com.pe/blog/', 'priority': '0.7', 'changefreq': 'weekly'},
        {'url': 'https://minerafidami.com.pe/carreras/', 'priority': '0.7', 'changefreq': 'weekly'},
        {'url': 'https://minerafidami.com.pe/contacto/', 'priority': '0.6', 'changefreq': 'monthly'},
    ]
    
    # Fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
    # Generar XML del sitemap
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    
    # Agregar URLs estáticas
    for url_info in urls_estaticas:
        xml_content += f'''  <url>
    <loc>{url_info['url']}</loc>
    <lastmod>{fecha_actual}</lastmod>
    <changefreq>{url_info['changefreq']}</changefreq>
    <priority>{url_info['priority']}</priority>
  </url>
'''
    
    # Cerrar XML
    xml_content += '''</urlset>'''
    
    # Crear directorio static si no existe
    static_dir = 'static'
    os.makedirs(static_dir, exist_ok=True)
    
    # Guardar sitemap
    sitemap_path = os.path.join(static_dir, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"✅ Sitemap generado exitosamente en {sitemap_path}")
    print(f"📄 Tamaño: {len(xml_content)} bytes")
    print(f"🔗 URLs incluidas: {len(urls_estaticas)}")
    
    # Mostrar contenido
    print("\n📋 Contenido del sitemap:")
    print(xml_content)
    
    return sitemap_path

if __name__ == '__main__':
    generar_sitemap_manual() 