from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
import re


class ConfiguracionGeneral(models.Model):
    """Configuración general del sitio web"""
    nombre_empresa = models.CharField(max_length=255, default="Minera Fidami S.A.")
    slogan = models.TextField(blank=True, null=True, default="Líderes en Minería Sostenible y Eficiente")
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    valores = models.JSONField(default=list, blank=True)
    logo = models.ImageField(upload_to='configuracion/', blank=True, null=True, help_text="Logo de la empresa (recomendado: PNG, SVG)")
    logo_url = models.URLField(blank=True, null=True, help_text="URL externa del logo (alternativa)")
    favicon = models.ImageField(upload_to='configuracion/', blank=True, null=True, help_text="Favicon de la empresa (recomendado: ICO, PNG)")
    favicon_url = models.URLField(blank=True, null=True, help_text="URL externa del favicon (alternativa)")
    email_contacto = models.EmailField(blank=True, null=True, default="recepcion@minerafidami.com.pe")
    telefono_principal = models.CharField(max_length=50, blank=True, null=True, default="+51 914599576")
    direccion_oficina = models.TextField(blank=True, null=True, default="Sancos Lucanas, Ayacucho")
    coordenadas_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    coordenadas_lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    horario_atencion = models.CharField(max_length=255, blank=True, null=True)
    meta_title_default = models.CharField(max_length=255, blank=True, null=True)
    meta_description_default = models.TextField(blank=True, null=True)
    meta_keywords_default = models.TextField(blank=True, null=True)
    google_analytics_id = models.CharField(max_length=50, blank=True, null=True)
    facebook_pixel_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración General"
        verbose_name_plural = "Configuración General"

    def __str__(self):
        return self.nombre_empresa

    def get_logo_url(self):
        """Retorna la URL del logo con prioridad para archivos subidos"""
        if self.logo:
            return self.logo.url
        elif self.logo_url:
            return self.logo_url
        return None

    def get_favicon_url(self):
        """Retorna la URL del favicon con prioridad para archivos subidos"""
        if self.favicon:
            return self.favicon.url
        elif self.favicon_url:
            return self.favicon_url
        return None


class Pagina(models.Model):
    """Páginas del sitio web"""
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('borrador', 'Borrador'),
    ]

    slug = models.SlugField(max_length=255, unique=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    imagen_principal = models.URLField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pagina_detail', kwargs={'slug': self.slug})


class Testimonio(models.Model):
    """Testimonios de clientes y colaboradores"""
    nombre = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    testimonio = models.TextField()
    calificacion = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    imagen = models.ImageField(upload_to='testimonios/', blank=True, null=True, help_text="Imagen subida al servidor (recomendado: JPG, PNG)")
    imagen_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen (alternativa)")
    proyecto_relacionado = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"

    def get_imagen_url(self):
        """Retorna la URL de la imagen con prioridad para archivos subidos"""
        if self.imagen:
            return self.imagen.url
        elif self.imagen_url:
            return self.imagen_url
        return None


class Equipo(models.Model):
    """Personal de la empresa"""
    slug = models.SlugField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    experiencia_anos = models.IntegerField(blank=True, null=True)
    especialidades = models.JSONField(default=list, blank=True)
    educacion = models.JSONField(default=list, blank=True)
    certificaciones = models.JSONField(default=list, blank=True)
    foto = models.ImageField(upload_to='equipo/', blank=True, null=True, help_text="Foto subida al servidor (recomendado: JPG, PNG)")
    foto_url = models.URLField(blank=True, null=True, help_text="URL externa de la foto (alternativa)")
    email = models.EmailField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    directivo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Miembro del Equipo"
        verbose_name_plural = "Miembros del Equipo"
        ordering = ['orden', 'apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

    def get_absolute_url(self):
        return reverse('core:equipo_detail', kwargs={'slug': self.slug})

    def get_foto_url(self):
        """Retorna la URL de la foto con prioridad para archivos subidos"""
        if self.foto:
            return self.foto.url
        elif self.foto_url:
            return self.foto_url
        return None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.nombre} {self.apellido}")
        super().save(*args, **kwargs)


class CertificacionPremio(models.Model):
    """Certificaciones y premios de la empresa"""
    TIPO_CHOICES = [
        ('certificacion', 'Certificación'),
        ('premio', 'Premio'),
        ('reconocimiento', 'Reconocimiento'),
    ]

    slug = models.SlugField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    organismo_otorgante = models.CharField(max_length=255, blank=True, null=True)
    fecha_otorgamiento = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    url_logo = models.URLField(blank=True, null=True, help_text="URL del logo de la certificación")
    url_documento = models.URLField(blank=True, null=True, help_text="URL del documento de la certificación")
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('vencido', 'Vencido'), ('suspendido', 'Suspendido')], default='activo')
    orden = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Certificación/Premio"
        verbose_name_plural = "Certificaciones y Premios"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_display()}"

    def get_absolute_url(self):
        return reverse('core:certificacion_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class RedSocial(models.Model):
    """Redes sociales de la empresa"""
    REDES_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter/X'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('tiktok', 'TikTok'),
        ('github', 'GitHub'),
        ('website', 'Sitio Web'),
    ]
    
    nombre = models.CharField(max_length=50, choices=REDES_CHOICES)
    url = models.URLField()
    icono = models.CharField(max_length=50, blank=True, null=True, help_text="Clase CSS del icono (opcional)")
    color = models.CharField(max_length=7, blank=True, null=True, help_text="Color hexadecimal (ej: #1877F2)")
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ['orden', 'nombre']
        unique_together = ['nombre']

    def __str__(self):
        return self.get_nombre_display()

    def get_icon_class(self):
        """Retorna la clase CSS del icono según la red social"""
        iconos = {
            'facebook': 'fab fa-facebook-f',
            'twitter': 'fab fa-twitter',
            'linkedin': 'fab fa-linkedin-in',
            'instagram': 'fab fa-instagram',
            'youtube': 'fab fa-youtube',
            'whatsapp': 'fab fa-whatsapp',
            'telegram': 'fab fa-telegram-plane',
            'tiktok': 'fab fa-tiktok',
            'github': 'fab fa-github',
            'website': 'fas fa-globe',
        }
        return iconos.get(self.nombre, 'fas fa-link')

    def get_color(self):
        """Retorna el color por defecto según la red social"""
        colores = {
            'facebook': '#1877F2',
            'twitter': '#1DA1F2',
            'linkedin': '#0077B5',
            'instagram': '#E4405F',
            'youtube': '#FF0000',
            'whatsapp': '#25D366',
            'telegram': '#0088CC',
            'tiktok': '#000000',
            'github': '#333333',
            'website': '#6B7280',
        }
        return self.color or colores.get(self.nombre, '#6B7280')


class HeroSection(models.Model):
    """Configuración del hero section de la página de inicio"""
    titulo_principal = models.CharField(max_length=255, default="HACIENDO LO COMPLEJO SIMPLE")
    subtitulo = models.TextField(default="Líderes en minería sostenible y eficiente. Comprometidos con la seguridad, la innovación y el respeto al medio ambiente.")
    imagen_fondo = models.ImageField(upload_to='hero_sections/', blank=True, null=True, help_text="Imagen de fondo subida al servidor (recomendado: JPG, PNG)")
    imagen_fondo_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen de fondo (alternativa)")
    texto_boton_principal = models.CharField(max_length=100, default="Contáctanos")
    url_boton_principal = models.CharField(max_length=255, default="contacto")
    texto_boton_secundario = models.CharField(max_length=100, default="Explora nuestros proyectos")
    url_boton_secundario = models.CharField(max_length=255, default="proyectos")
    activo = models.BooleanField(default=True)
    orden = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"
        ordering = ['orden']

    def __str__(self):
        return f"Hero Section {self.orden} - {self.titulo_principal}"

    def get_absolute_url(self):
        return reverse('core:home')

    def get_imagen_fondo_url(self):
        """Retorna la URL de la imagen de fondo con prioridad para archivos subidos"""
        if self.imagen_fondo:
            return self.imagen_fondo.url
        elif self.imagen_fondo_url:
            return self.imagen_fondo_url
        return None


class Mensaje(models.Model):
    """Mensajes del sistema (alertas, notificaciones, etc.)"""
    TIPO_CHOICES = [
        ('info', 'Información'),
        ('success', 'Éxito'),
        ('warning', 'Advertencia'),
        ('error', 'Error'),
    ]
    
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='info')
    activo = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['orden', '-created_at']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.titulo}"

    def esta_activo(self):
        """Verifica si el mensaje está activo según las fechas"""
        ahora = timezone.now()
        if not self.activo:
            return False
        if self.fecha_inicio and ahora < self.fecha_inicio:
            return False
        if self.fecha_fin and ahora > self.fecha_fin:
            return False
        return True
