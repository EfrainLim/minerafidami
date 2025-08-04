#!/bin/bash

echo "🔧 Solucionando problema del sitemap..."

# 1. Verificar que Django está funcionando
echo "📊 Verificando Django..."
python manage.py check

# 2. Ejecutar script de verificación
echo "🔍 Ejecutando verificación de sitemap..."
python verificar_sitemap.py

# 3. Verificar que el sitemap es accesible
echo "🌐 Verificando acceso al sitemap..."
curl -I http://localhost:8005/sitemap.xml

# 4. Verificar robots.txt
echo "🤖 Verificando robots.txt..."
curl -I http://localhost:8005/robots.txt

# 5. Verificar logs de Nginx
echo "📋 Verificando logs de Nginx..."
tail -n 10 /var/log/nginx/minerafidami_error.log

# 6. Verificar configuración de Nginx
echo "🔍 Verificando configuración de Nginx..."
grep -n "sitemap" /etc/nginx/sites-available/minerafidami.com.pe

# 7. Reiniciar servicios si es necesario
echo "🔄 Reiniciando servicios..."
systemctl restart gunicorn
systemctl restart nginx

echo "✅ Verificación completada"
echo "🌐 Prueba acceder a: https://minerafidami.com.pe/sitemap.xml" 