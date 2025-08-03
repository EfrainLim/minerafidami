"""
Configuración SEO para Minera Fidami S.A.
"""

# Configuración de Google Analytics
GOOGLE_ANALYTICS_ID = 'GA_MEASUREMENT_ID'  # Reemplazar con tu ID real

# Configuración de Google Search Console
GOOGLE_SEARCH_CONSOLE_VERIFICATION = 'TU_CODIGO_DE_VERIFICACION'  # Reemplazar con tu código

# Configuración de redes sociales
SOCIAL_MEDIA = {
    'linkedin': 'https://www.linkedin.com/company/minera-fidami',
    'facebook': 'https://www.facebook.com/minerafidami',
    'twitter': 'https://twitter.com/minerafidami',
    'youtube': 'https://www.youtube.com/@minerafidami',
}

# Palabras clave principales
MAIN_KEYWORDS = [
    'minería',
    'minería sostenible',
    'minería Perú',
    'exploración minera',
    'explotación minera',
    'minería responsable',
    'oro Perú',
    'minerales',
    'minería Ayacucho',
    'Fidami',
    'minería subterránea',
    'minería cielo abierto',
]

# Configuración de sitemap
SITEMAP_CONFIG = {
    'static_priority': 1.0,
    'static_changefreq': 'weekly',
    'content_priority': 0.8,
    'content_changefreq': 'monthly',
    'blog_priority': 0.6,
    'blog_changefreq': 'weekly',
}

# Configuración de robots.txt
ROBOTS_CONFIG = {
    'crawl_delay': 1,
    'disallow': [
        '/admin/',
        '/static/admin/',
        '/media/admin/',
        '/private/',
    ],
    'allow': [
        '/servicios/',
        '/proyectos/',
        '/blog/',
        '/carreras/',
        '/contacto/',
        '/innovacion/',
        '/responsabilidad-social/',
    ]
} 