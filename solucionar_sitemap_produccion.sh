#!/bin/bash

echo "🔧 Solucionando problema del sitemap en producción..."

# 1. Ir al directorio del proyecto
cd /root/minerafidami

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Generar sitemap estáticamente
echo "📄 Generando sitemap.xml..."
python manage.py generate_sitemap

# 4. Generar robots.txt estáticamente
echo "🤖 Generando robots.txt..."
cat > static/robots.txt << 'EOF'
User-agent: *
Allow: /

# Sitemap
Sitemap: https://minerafidami.com.pe/sitemap.xml

# Disallow admin and private areas
Disallow: /admin/
Disallow: /static/admin/
Disallow: /media/admin/

# Allow important pages
Allow: /servicios/
Allow: /proyectos/
Allow: /blog/
Allow: /carreras/
Allow: /contacto/

# Crawl delay (opcional)
Crawl-delay: 1
EOF

# 5. Verificar que los archivos se crearon
echo "🔍 Verificando archivos generados..."
ls -la static/sitemap.xml
ls -la static/robots.txt

# 6. Verificar contenido del sitemap
echo "📋 Contenido del sitemap:"
head -20 static/sitemap.xml

# 7. Actualizar configuración de Nginx
echo "🔧 Actualizando configuración de Nginx..."
cat > /etc/nginx/sites-available/minerafidami.com.pe << 'EOF'
# Configuración de Nginx para Minera Fidami
server {
    listen 80;
    server_name minerafidami.com.pe www.minerafidami.com.pe;
    
    # Archivos estáticos
    location /static/ {
        alias /root/minerafidami/staticfiles/;
        expires 1y;
    }
    
    # Archivos media
    location /media/ {
        alias /root/minerafidami/media/;
        expires 1y;
    }
    
    # Sitemap y robots.txt estáticos
    location = /sitemap.xml {
        alias /root/minerafidami/static/sitemap.xml;
        expires 1d;
        add_header Content-Type application/xml;
    }
    
    location = /robots.txt {
        alias /root/minerafidami/static/robots.txt;
        expires 1d;
        add_header Content-Type text/plain;
    }
    
    # Django (puerto 8005)
    location / {
        proxy_pass http://127.0.0.1:8005;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Logs
    access_log /var/log/nginx/minerafidami_access.log;
    error_log /var/log/nginx/minerafidami_error.log;
}
EOF

# 8. Verificar y reiniciar Nginx
echo "🔄 Reiniciando Nginx..."
nginx -t
systemctl restart nginx

# 9. Verificar que funciona
echo "🌐 Verificando acceso..."
curl -I http://minerafidami.com.pe/sitemap.xml
curl -I http://minerafidami.com.pe/robots.txt

echo "✅ ¡Sitemap solucionado!"
echo "🌐 Sitemap disponible en: https://minerafidami.com.pe/sitemap.xml"
echo "🤖 Robots.txt disponible en: https://minerafidami.com.pe/robots.txt" 