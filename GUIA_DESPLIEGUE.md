# 🚀 Guía de Despliegue
## Minera Fidami S.A.

### 📋 Información
- **IP**: 64.23.222.197
- **Dominio**: minerafidami.com.pe
- **Puerto**: 8005
- **Ruta**: /root/minerafidami/

---

## 🔧 Pasos de Despliegue

### 1. Preparar el proyecto localmente
```bash
# Asegúrate de estar en el directorio del proyecto
cd /ruta/a/tu/proyecto/minera-fidami

# Verificar que estás en el directorio correcto
ls -la
# Deberías ver: manage.py, minerafidami/, core/, servicios/, etc.
```

### 2. Crear directorio en el servidor
```bash
# Conectar al servidor
ssh root@64.23.222.197

# Crear directorio del proyecto
mkdir -p /root/minerafidami

# Verificar que se creó
ls -la /root/
```

### 3. Subir archivos del proyecto
```bash
# Desde tu máquina local (en otra terminal)
# Asegúrate de estar en el directorio del proyecto
cd /ruta/a/tu/proyecto/minera-fidami

# Copiar todo el proyecto al servidor
scp -r ./* root@64.23.222.197:/root/minerafidami/

# O si prefieres copiar archivo por archivo:
scp -r manage.py root@64.23.222.197:/root/minerafidami/
scp -r minerafidami/ root@64.23.222.197:/root/minerafidami/
scp -r core/ root@64.23.222.197:/root/minerafidami/
scp -r servicios/ root@64.23.222.197:/root/minerafidami/
scp -r proyectos/ root@64.23.222.197:/root/minerafidami/
scp -r blog/ root@64.23.222.197:/root/minerafidami/
scp -r carreras/ root@64.23.222.197:/root/minerafidami/
scp -r contacto/ root@64.23.222.197:/root/minerafidami/
scp -r innovacion/ root@64.23.222.197:/root/minerafidami/
scp -r rsocial/ root@64.23.222.197:/root/minerafidami/
scp -r theme/ root@64.23.222.197:/root/minerafidami/
scp -r templates/ root@64.23.222.197:/root/minerafidami/
scp -r static/ root@64.23.222.197:/root/minerafidami/
scp -r media/ root@64.23.222.197:/root/minerafidami/
scp requirements.txt root@64.23.222.197:/root/minerafidami/
scp requirements_produccion.txt root@64.23.222.197:/root/minerafidami/
scp GUIA_DESPLIEGUE.md root@64.23.222.197:/root/minerafidami/
scp config_produccion.txt root@64.23.222.197:/root/minerafidami/
```

### 4. Verificar archivos en el servidor
```bash
# Conectar al servidor
ssh root@64.23.222.197

# Ir al directorio del proyecto
cd /root/minerafidami

# Verificar que todos los archivos están ahí
ls -la

# Verificar estructura del proyecto
tree -L 2
# O si no tienes tree:
find . -maxdepth 2 -type d

# Verificar archivos importantes
ls -la manage.py
ls -la minerafidami/settings.py
ls -la requirements.txt
ls -la requirements_produccion.txt
ls -la GUIA_DESPLIEGUE.md
```

### 5. Conectar al servidor
```bash
ssh root@64.23.222.197
cd /root/minerafidami
```

### 6. Instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_produccion.txt
```

### 7. Configurar producción
```bash
# Cambiar DEBUG = False en settings.py
nano minerafidami/settings.py
# Buscar: DEBUG = True
# Cambiar a: DEBUG = False
```

### 8. Compilar y preparar
```bash
# Compilar Tailwind CSS
python manage.py tailwind build

# Migraciones
python manage.py migrate

# Archivos estáticos
python manage.py collectstatic --noinput

# Verificar configuración
python manage.py check --deploy
```

### 9. Configurar Gunicorn

#### Crear archivo de configuración
```bash
cat > gunicorn.conf.py << 'EOF'
# Configuración de Gunicorn para Minera Fidami
# Puerto: 8005

# Puerto del servidor
bind = "0.0.0.0:8005"

# Número de workers (procesos)
workers = 3

# Timeout
timeout = 30

# Logs
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
loglevel = "info"

# Configuración de seguridad
limit_request_line = 4094
limit_request_fields = 100
EOF
```

#### Crear servicio de Gunicorn
```bash
cat > /etc/systemd/system/gunicorn.service << 'EOF'
[Unit]
Description=Gunicorn para Minera Fidami
After=network.target

[Service]
User=root
WorkingDirectory=/root/minerafidami
Environment="PATH=/root/minerafidami/venv/bin"
ExecStart=/root/minerafidami/venv/bin/gunicorn --config gunicorn.conf.py minerafidami.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Habilitar y iniciar
systemctl daemon-reload
systemctl enable gunicorn
systemctl start gunicorn
```

### 10. Configurar Nginx

#### Instalar Nginx
```bash
apt update
apt install nginx
```

#### Crear configuración de Nginx (sin SSL inicialmente)
```bash
cat > /etc/nginx/sites-available/minerafidami.com.pe << 'EOF'
# Configuración de Nginx para Minera Fidami
# Archivo: /etc/nginx/sites-available/minerafidami.com.pe

# Servidor HTTP (sin SSL inicialmente)
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

# Habilitar sitio
ln -s /etc/nginx/sites-available/minerafidami.com.pe /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default

# Verificar y reiniciar
nginx -t
systemctl restart nginx
```

### 11. Configurar SSL
```bash
# Instalar Certbot
apt install certbot python3-certbot-nginx

# Obtener certificado (esto actualizará automáticamente la configuración de Nginx)
certbot --nginx -d minerafidami.com.pe -d www.minerafidami.com.pe
```

### 12. Verificar que todo funciona
```bash
# Verificar estado de servicios
systemctl status gunicorn nginx

# Verificar que el sitio responde
curl -I http://minerafidami.com.pe

# Verificar logs si hay problemas
journalctl -u gunicorn -f
tail -f /var/log/nginx/minerafidami_error.log
```

---

## 🔧 Comandos Útiles

### Verificar estado
```bash
systemctl status gunicorn nginx
```

### Ver logs
```bash
journalctl -u gunicorn -f
tail -f /var/log/nginx/minerafidami_error.log
```

### Reiniciar servicios
```bash
systemctl restart gunicorn nginx
```

### Backup de base de datos
```bash
cp /root/minerafidami/db.sqlite3 backup_$(date +%Y%m%d).sqlite3
```

---

## ✅ Checklist

- [ ] Proyecto preparado localmente
- [ ] Directorio creado en servidor (/root/minerafidami/)
- [ ] Archivos transferidos al servidor
- [ ] Estructura del proyecto verificada
- [ ] Dependencias instaladas
- [ ] DEBUG = False en settings.py
- [ ] Migraciones ejecutadas
- [ ] Archivos estáticos recolectados
- [ ] Gunicorn configurado y ejecutándose
- [ ] Nginx configurado y ejecutándose
- [ ] SSL configurado
- [ ] Sitio accesible en https://minerafidami.com.pe

---

## 🆘 Solución de Problemas

### Error 502
```bash
systemctl status gunicorn
journalctl -u gunicorn -f
```

### Error de permisos
```bash
chown -R root:root /root/minerafidami
chmod -R 755 /root/minerafidami
```

### Error de SSL
```bash
certbot --nginx -d minerafidami.com.pe
```

### Error al transferir archivos
```bash
# Si hay problemas de permisos
chmod -R 755 /ruta/a/tu/proyecto/minera-fidami

# Si hay problemas de conexión
scp -v -r ./* root@64.23.222.197:/root/minerafidami/

# Si necesitas comprimir antes de transferir
tar -czf minera-fidami.tar.gz ./*
scp minera-fidami.tar.gz root@64.23.222.197:/root/
# En el servidor:
cd /root
tar -xzf minera-fidami.tar.gz
mv minera-fidami/* /root/minerafidami/
rm -rf minera-fidami minera-fidami.tar.gz
```

### Error de Nginx SSL
```bash
# Si Nginx falla por certificados SSL inexistentes:
# 1. Usar configuración sin SSL primero
# 2. Verificar configuración
nginx -t

# 3. Reiniciar Nginx
systemctl restart nginx

# 4. Obtener certificados SSL
certbot --nginx -d minerafidami.com.pe

# 5. Verificar que Nginx funciona
systemctl status nginx
```

### Error de Gunicorn
```bash
# Verificar logs de Gunicorn
journalctl -u gunicorn -f

# Reiniciar Gunicorn
systemctl restart gunicorn

# Verificar que está ejecutándose
systemctl status gunicorn
```

---

**¡Despliegue completado! 🎯** 