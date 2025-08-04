#!/bin/bash

echo "🔧 Generando sitemap en producción..."

# 1. Ir al directorio del proyecto
cd /root/minerafidami

# 2. Generar sitemap
python generar_sitemap_manual.py

# 3. Generar robots.txt
cat > static/robots.txt << 'EOF'
User-agent: *
Allow: /

# Sitemap
Sitemap: https://minerafidami.com.pe/sitemap.xml

# Disallow admin
Disallow: /admin/

# Allow important pages
Allow: /servicios/
Allow: /proyectos/
Allow: /blog/
Allow: /carreras/
Allow: /contacto/
EOF

# 4. Verificar archivos
echo "📋 Archivos generados:"
ls -la static/sitemap.xml
ls -la static/robots.txt

echo "✅ ¡Sitemap listo!"
echo "🌐 Accede a: https://minerafidami.com.pe/sitemap.xml" 