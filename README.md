# Minera Fidami S.A. - Sitio Web Corporativo

Sitio web empresarial moderno y elegante para **Minera Fidami S.A.**, especializada en **Minería Subterránea**. Desarrollado con Django y Tailwind CSS.

## 🚀 Características Principales

- **Diseño Moderno**: Interfaz elegante y profesional con Tailwind CSS
- **Completamente Administrable**: Panel de administración Django para gestionar todo el contenido
- **Responsive**: Diseño adaptativo para todos los dispositivos
- **SEO Optimizado**: Meta tags, URLs amigables y estructura semántica
- **Múltiples Secciones**: Inicio, Sobre Nosotros, Servicios, Proyectos, Innovación, Responsabilidad Social, Blog, Carreras, Contacto
- **Formularios Interactivos**: Contacto, Newsletter, Postulaciones
- **Galerías de Imágenes**: Soporte para multimedia con prioridad de servidor
- **Sistema de Blog**: Gestión de noticias y artículos
- **Gestión de Vacantes**: Sistema completo de carreras
- **Paginación Profesional**: Navegación elegante en listas
- **Filtros Avanzados**: Por categorías y tipos

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.4
- **Frontend**: Tailwind CSS
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Lenguaje**: Python 3.13
- **Framework CSS**: Django-Tailwind
- **Iconos**: Font Awesome 6.4.0

## 📋 Requisitos Previos

- Python 3.8+
- pip
- Node.js (para Tailwind CSS)

## 🔧 Instalación

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd minera-fidami
```

### 2. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Tailwind CSS
```bash
cd theme
npm install
npm run build
cd ..
```

### 5. Configurar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

El sitio estará disponible en `http://localhost:8000`

## 📁 Estructura del Proyecto

```
minerafidami/
├── core/                 # Aplicación principal
│   ├── models.py        # Modelos: Configuración, Páginas, Equipo, etc.
│   ├── views.py         # Vistas principales
│   ├── admin.py         # Configuración del admin
│   ├── signals.py       # Señales para gestión de archivos
│   └── context_processors.py # Procesadores de contexto
├── servicios/           # Gestión de servicios
├── proyectos/           # Gestión de proyectos (simplificado)
├── innovacion/          # Tecnologías, proyectos y patentes
├── rsocial/            # Responsabilidad social
├── blog/               # Sistema de blog y noticias
├── carreras/           # Gestión de vacantes
├── contacto/           # Formularios de contacto
├── theme/              # Configuración de Tailwind CSS
├── templates/          # Plantillas HTML
├── static/             # Archivos estáticos
└── media/              # Archivos subidos por usuarios
```

## 🎨 Personalización

### Colores
Los colores principales están definidos en `theme/static_src/src/styles/input.css`:
- **Naranja Principal**: #ff6b35
- **Naranja Dorado**: #f7931e
- **Negro Profundo**: #1a1a1a
- **Gris Oscuro**: #2d2d2d

### Configuración General
Accede al admin de Django (`/admin/`) para configurar:
- Información de la empresa
- Contacto
- Redes sociales
- SEO
- Analytics

## 📝 Uso del Panel de Administración

### 1. Configuración General
- **Configuración General**: Datos de la empresa, contacto, SEO, logo, favicon
- **Páginas**: Crear páginas estáticas
- **Equipo**: Gestionar miembros del equipo
- **Testimonios**: Agregar testimonios de clientes
- **Certificaciones**: Gestionar certificaciones y premios
- **Hero Sections**: Sliders dinámicos para la página principal
- **Mensajes**: Mensajes del sistema
- **Redes Sociales**: Iconos de redes sociales dinámicos

### 2. Contenido
- **Servicios**: Crear y gestionar servicios
- **Proyectos**: Gestionar proyectos mineros (solo categorías)
- **Innovación**: Tecnologías, proyectos de innovación, patentes
- **Responsabilidad Social**: Programas, alianzas, impactos, reportes
- **Blog**: Publicar noticias y artículos
- **Vacantes**: Crear ofertas de trabajo

### 3. Comunicación
- **Contactos**: Ver mensajes recibidos
- **Newsletter**: Gestionar suscriptores
- **Postulaciones**: Revisar candidatos

## 🚀 Despliegue en Producción

### 1. Configurar variables de entorno
```bash
export SECRET_KEY='tu-clave-secreta'
export DEBUG=False
export ALLOWED_HOSTS='tu-dominio.com'
```

### 2. Configurar base de datos PostgreSQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'minerafidami',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Configurar archivos estáticos
```bash
python manage.py collectstatic
```

### 4. Configurar servidor web (Nginx + Gunicorn)
```bash
pip install gunicorn
gunicorn minerafidami.wsgi:application
```

## 📱 Características Responsive

- **Mobile First**: Diseño optimizado para móviles
- **Tablet**: Adaptación para tablets
- **Desktop**: Experiencia completa en escritorio
- **Navegación**: Menú hamburguesa en móviles

## 🔍 SEO y Performance

- **Meta Tags**: Automáticos y configurables
- **URLs Amigables**: Slugs automáticos
- **Imágenes Optimizadas**: Soporte para WebP
- **Lazy Loading**: Carga diferida de imágenes
- **Compresión**: CSS y JS minificados

## 📊 Estado Actual del Proyecto

### ✅ Completado (95%)
- **Aplicaciones**: 8 aplicaciones completas
- **Modelos**: 20 modelos de base de datos
- **Plantillas**: 16 plantillas HTML
- **Vistas**: 40+ vistas implementadas
- **URLs**: 35+ URLs funcionales
- **Admin**: Panel completo para todos los modelos
- **Funcionalidades**: Paginación, filtros, formularios, galerías

### 🚧 En Progreso (5%)
- **Optimizaciones**: Performance y velocidad
- **Mejoras UX**: Animaciones y transiciones
- **Contenido**: Datos reales de la empresa

## 🎯 URLs Funcionales

### ✅ Páginas Principales
- `/` - Página de inicio
- `/admin/` - Panel de administración
- `/sobre-nosotros/` - Sobre nosotros
- `/contacto/` - Formulario de contacto

### ✅ Servicios
- `/servicios/` - Lista de servicios
- `/servicios/<slug>/` - Detalle de servicio

### ✅ Proyectos
- `/proyectos/` - Lista de proyectos (con paginación)
- `/proyectos/<slug>/` - Detalle de proyecto

### ✅ Innovación
- `/innovacion/` - Página principal
- `/innovacion/tecnologias/` - Lista de tecnologías
- `/innovacion/proyectos/` - Lista de proyectos de innovación
- `/innovacion/patentes/` - Lista de patentes

### ✅ Responsabilidad Social
- `/responsabilidad-social/` - Página principal
- `/responsabilidad-social/programas/` - Lista de programas
- `/responsabilidad-social/alianzas/` - Lista de alianzas
- `/responsabilidad-social/impactos-ambientales/` - Lista de impactos
- `/responsabilidad-social/reportes/` - Lista de reportes

### ✅ Blog
- `/blog/` - Lista de artículos
- `/blog/<slug>/` - Detalle de artículo

### ✅ Carreras
- `/carreras/` - Lista de vacantes
- `/carreras/<slug>/` - Detalle de vacante

## 🏭 Características Específicas para Minería Subterránea

### 🎯 Contenido Especializado
- **Tecnologías de perforación** subterránea
- **Sistemas de ventilación** y seguridad
- **Métodos de extracción** (corte y relleno, hundimiento, etc.)
- **Equipos especializados** para minería subterránea

### 📊 Indicadores de Rendimiento
- **Toneladas extraídas** por día/mes
- **Profundidad de operaciones**
- **Eficiencia energética** en operaciones subterráneas
- **Tasa de recuperación** de minerales

### 🛡️ Seguridad y Certificaciones
- **Protocolos de seguridad** subterránea
- **Certificaciones ISO** específicas para minería
- **Equipos de rescate** y emergencia
- **Capacitación continua** del personal

## 📞 Soporte

Para soporte técnico o consultas sobre el proyecto:
- Email: soporte@minerafidami.com.pe
- Teléfono: +51 914599576

## 📄 Licencia

Este proyecto es propiedad de Minera Fidami S.A. Todos los derechos reservados.

---

**Desarrollado con ❤️ para Minera Fidami S.A.** 
**Especialistas en Minería Subterránea** 🏭 