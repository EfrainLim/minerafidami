# ✅ Checklist SEO - Minera Fidami S.A.

## 🎯 **Checklist Rápido para Aparecer en Google**

---

## 📋 **PRE-PUBLICACIÓN (Hacer ANTES de subir al servidor)**

### ✅ **1. Configurar Google Analytics**
- [ ] Crear cuenta en https://analytics.google.com/
- [ ] Obtener ID de medición (G-XXXXXXXXXX)
- [ ] Editar `core/seo_config.py` con tu ID
- [ ] Editar `templates/base.html` con tu ID

### ✅ **2. Configurar Google Search Console**
- [ ] Crear cuenta en https://search.google.com/search-console
- [ ] Agregar propiedad de tu sitio web
- [ ] Obtener código de verificación
- [ ] Editar `core/seo_config.py` con tu código
- [ ] Editar `templates/base.html` con tu código

### ✅ **3. Configurar Dominio**
- [ ] Editar `minerafidami/settings.py` con tu dominio
- [ ] Configurar ALLOWED_HOSTS
- [ ] Configurar HTTPS (recomendado)

---

## 🚀 **PUBLICACIÓN (Al subir al servidor)**

### ✅ **4. Subir Archivos**
- [ ] Subir todos los archivos al servidor
- [ ] Configurar base de datos
- [ ] Ejecutar migraciones
- [ ] Configurar variables de entorno

### ✅ **5. Configurar Servidor Web**
- [ ] Configurar Apache o Nginx
- [ ] Configurar SSL/HTTPS
- [ ] Configurar archivos estáticos
- [ ] Verificar que el sitio funcione

---

## 🔍 **POST-PUBLICACIÓN (Después de subir)**

### ✅ **6. Verificar Implementación**
- [ ] Visitar `https://tudominio.com/sitemap.xml`
- [ ] Visitar `https://tudominio.com/robots.txt`
- [ ] Verificar meta tags en el código fuente
- [ ] Verificar que Google Analytics funcione
- [ ] Verificar que Search Console esté verificado

### ✅ **7. Enviar a Google**
- [ ] En Search Console, enviar sitemap
- [ ] Solicitar indexación de páginas principales
- [ ] Verificar que no haya errores en Search Console

---

## 📊 **MONITOREO (Continuo)**

### ✅ **8. Monitoreo Diario**
- [ ] Revisar Google Search Console
- [ ] Verificar errores de rastreo
- [ ] Revisar consultas de búsqueda

### ✅ **9. Monitoreo Semanal**
- [ ] Revisar Google Analytics
- [ ] Analizar tráfico orgánico
- [ ] Optimizar contenido basado en datos

### ✅ **10. Monitoreo Mensual**
- [ ] Revisar posiciones en Google
- [ ] Actualizar contenido
- [ ] Optimizar velocidad del sitio

---

## 🎯 **PALABRAS CLAVE A MONITOREAR**

### **Primarias:**
- [ ] minería Perú
- [ ] minería sostenible
- [ ] exploración minera
- [ ] explotación minera

### **Secundarias:**
- [ ] minería responsable
- [ ] oro Perú
- [ ] minería Ayacucho
- [ ] Fidami

---

## 📈 **EXPECTATIVAS DE TIEMPO**

| Actividad | Tiempo Esperado |
|-----------|-----------------|
| Primera detección | 1-7 días |
| Primera indexación | 1-4 semanas |
| Posicionamiento inicial | 2-8 semanas |
| Resultados significativos | 3-6 meses |

---

## 🔧 **COMANDOS ÚTILES**

```bash
# Verificar sitemap
curl https://tudominio.com/sitemap.xml

# Verificar robots.txt
curl https://tudominio.com/robots.txt

# Generar sitemap manualmente
python manage.py shell
>>> from django.contrib.sitemaps import ping_google
>>> ping_google()
```

---

## 📞 **CONTACTOS DE AYUDA**

- **Google Analytics:** https://support.google.com/analytics/
- **Google Search Console:** https://support.google.com/webmasters/
- **Google PageSpeed:** https://pagespeed.web.dev/

---

## 🎉 **¡LISTO!**

Una vez completado este checklist, tu sitio web estará completamente optimizado para aparecer en Google.

**¡El SEO está configurado para el éxito!** 🚀 