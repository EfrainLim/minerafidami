#!/bin/bash

echo "🔧 Solucionando problema de Nginx SSL..."

# 1. Crear configuración de Nginx sin SSL
echo "📝 Creando configuración de Nginx sin SSL..."
cat > /etc/nginx/sites-available/minerafidami.com.pe << 'EOF'
# Configuración de Nginx para Minera Fidami (sin SSL)
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

# 2. Verificar configuración
echo "🔍 Verificando configuración de Nginx..."
nginx -t

# 3. Reiniciar Nginx
echo "🔄 Reiniciando Nginx..."
systemctl restart nginx

# 4. Verificar estado
echo "📊 Verificando estado de Nginx..."
systemctl status nginx

echo "✅ ¡Problema solucionado!"
echo "🌐 Ahora puedes acceder a: http://minerafidami.com.pe"
echo "🔒 Para agregar SSL, ejecuta: certbot --nginx -d minerafidami.com.pe" 