from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class CategoriaComunicado(models.Model):
    """Categorías para los comunicados"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default='#3B82F6', help_text="Color en formato hexadecimal")
    icono = models.CharField(max_length=50, default='fas fa-bullhorn', help_text="Clase de icono FontAwesome")
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría de Comunicado"
        verbose_name_plural = "Categorías de Comunicados"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class Comunicado(models.Model):
    """Comunicados oficiales de la empresa"""
    TIPO_CHOICES = [
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('informativo', 'Informativo'),
        ('evento', 'Evento'),
        ('mantenimiento', 'Mantenimiento'),
        ('seguridad', 'Seguridad'),
        ('operacional', 'Operacional'),
    ]
    
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('normal', 'Normal'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]

    # Información básica
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    resumen = models.TextField(blank=True, null=True, help_text="Resumen corto del comunicado")
    contenido = models.TextField()
    
    # Clasificación
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='informativo')
    categoria = models.ForeignKey(CategoriaComunicado, on_delete=models.SET_NULL, blank=True, null=True, related_name='comunicados')
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='normal')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='borrador')
    
    # Configuración de visualización
    mostrar_en_home = models.BooleanField(default=False, help_text="Mostrar como notificación en la página principal")
    mostrar_en_popup = models.BooleanField(default=False, help_text="Mostrar como popup emergente")
    destacado = models.BooleanField(default=False, help_text="Marcar como comunicado destacado")
    
    # Programación
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fecha_expiracion = models.DateTimeField(blank=True, null=True, help_text="Fecha hasta cuando mostrar el comunicado")
    activo = models.BooleanField(default=True)
    
    # Metadatos
    autor = models.CharField(max_length=100, blank=True, null=True)
    etiquetas = models.JSONField(default=list, blank=True, help_text="Etiquetas para categorización")
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    
    # Archivos adjuntos
    archivo_adjunto = models.FileField(upload_to='comunicados/adjuntos/', blank=True, null=True, help_text="Archivo PDF o documento adjunto")
    imagen_destacada = models.ImageField(upload_to='comunicados/imagenes/', blank=True, null=True, help_text="Imagen destacada del comunicado")
    
    # Estadísticas
    vistas = models.PositiveIntegerField(default=0)
    descargas = models.PositiveIntegerField(default=0)
    
    # Auditoría
    orden = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"
        ordering = ['-fecha_publicacion', '-prioridad', 'orden']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('comunicados:comunicado_detail', kwargs={'slug': self.slug})

    def esta_activo(self):
        """Verifica si el comunicado está activo según fechas y estado"""
        ahora = timezone.now()
        if not self.activo or self.estado != 'publicado':
            return False
        if self.fecha_publicacion and ahora < self.fecha_publicacion:
            return False
        if self.fecha_expiracion and ahora > self.fecha_expiracion:
            return False
        return True

    def incrementar_vista(self):
        """Incrementa el contador de vistas"""
        self.vistas += 1
        self.save(update_fields=['vistas'])

    def incrementar_descarga(self):
        """Incrementa el contador de descargas"""
        self.descargas += 1
        self.save(update_fields=['descargas'])

    def get_color_prioridad(self):
        """Retorna el color según la prioridad"""
        colores = {
            'baja': '#10B981',      # Verde
            'normal': '#3B82F6',    # Azul
            'alta': '#F59E0B',      # Amarillo
            'critica': '#EF4444',   # Rojo
        }
        return colores.get(self.prioridad, '#3B82F6')

    def get_icono_tipo(self):
        """Retorna el icono según el tipo"""
        iconos = {
            'urgente': 'fas fa-exclamation-triangle',
            'importante': 'fas fa-info-circle',
            'informativo': 'fas fa-newspaper',
            'evento': 'fas fa-calendar-alt',
            'mantenimiento': 'fas fa-tools',
            'seguridad': 'fas fa-shield-alt',
            'operacional': 'fas fa-cogs',
        }
        return iconos.get(self.tipo, 'fas fa-bullhorn')


class ComunicadoVista(models.Model):
    """Registro de vistas de comunicados para estadísticas"""
    comunicado = models.ForeignKey(Comunicado, on_delete=models.CASCADE, related_name='registro_vistas')
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    fecha_vista = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vista de Comunicado"
        verbose_name_plural = "Vistas de Comunicados"
        ordering = ['-fecha_vista']

    def __str__(self):
        return f"Vista de {self.comunicado.titulo} - {self.fecha_vista}"
