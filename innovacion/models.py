from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


class Tecnologia(models.Model):
    """Tecnologías innovadoras utilizadas en proyectos"""
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=[
        ('mineria', 'Minería'),
        ('ambiental', 'Ambiental'),
        ('seguridad', 'Seguridad'),
        ('eficiencia', 'Eficiencia Energética'),
        ('digital', 'Transformación Digital'),
    ])
    imagen_principal = models.ImageField(upload_to='tecnologias/', blank=True, null=True, help_text="Imagen principal subida al servidor (recomendado: JPG, PNG)")
    imagen_principal_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen principal (alternativa)")
    galeria_imagenes = models.JSONField(default=list, blank=True)
    video_url = models.URLField(blank=True, null=True)
    beneficios = models.JSONField(default=list, blank=True)
    aplicaciones = models.JSONField(default=list, blank=True)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], default='activo')
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    fecha_implementacion = models.DateField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('innovacion:tecnologia_detail', kwargs={'slug': self.slug})

    def get_imagen_principal_url(self):
        """Retorna la URL de la imagen principal con prioridad para archivos subidos"""
        if self.imagen_principal:
            return self.imagen_principal.url
        elif self.imagen_principal_url:
            return self.imagen_principal_url
        return None


class ProyectoInnovacion(models.Model):
    """Proyectos de innovación y desarrollo tecnológico"""
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    tipo_proyecto = models.CharField(max_length=100, choices=[
        ('investigacion', 'Investigación'),
        ('desarrollo', 'Desarrollo'),
        ('implementacion', 'Implementación'),
        ('colaboracion', 'Colaboración'),
    ])
    estado_proyecto = models.CharField(max_length=100, choices=[
        ('planificacion', 'Planificación'),
        ('desarrollo', 'En Desarrollo'),
        ('pruebas', 'En Pruebas'),
        ('implementado', 'Implementado'),
        ('finalizado', 'Finalizado'),
    ])
    tecnologias_utilizadas = models.JSONField(default=list, blank=True)
    equipo_investigacion = models.JSONField(default=list, blank=True)
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=10, default='PEN')
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin_estimada = models.DateField(blank=True, null=True)
    fecha_fin_real = models.DateField(blank=True, null=True)
    resultados = models.JSONField(default=list, blank=True)
    impacto_esperado = models.TextField(blank=True, null=True)
    imagen_principal = models.ImageField(upload_to='proyectos/', blank=True, null=True, help_text="Imagen principal subida al servidor (recomendado: JPG, PNG)")
    imagen_principal_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen principal (alternativa)")
    galeria_imagenes = models.JSONField(default=list, blank=True)
    video_url = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], default='activo')
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proyecto de Innovación"
        verbose_name_plural = "Proyectos de Innovación"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('innovacion:proyecto_detail', kwargs={'slug': self.slug})

    def get_imagen_principal_url(self):
        """Retorna la URL de la imagen principal con prioridad para archivos subidos"""
        if self.imagen_principal:
            return self.imagen_principal.url
        elif self.imagen_principal_url:
            return self.imagen_principal_url
        return None


class Patente(models.Model):
    """Patentes y propiedad intelectual"""
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    numero_patente = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=[
        ('patente', 'Patente'),
        ('marca', 'Marca Registrada'),
        ('derecho_autor', 'Derecho de Autor'),
        ('secreto_comercial', 'Secreto Comercial'),
    ])
    estado = models.CharField(max_length=100, choices=[
        ('solicitud', 'En Solicitud'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('vigente', 'Vigente'),
        ('expirada', 'Expirada'),
    ])
    fecha_solicitud = models.DateField(blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    fecha_expiracion = models.DateField(blank=True, null=True)
    inventores = models.JSONField(default=list, blank=True)
    aplicacion_industrial = models.TextField(blank=True, null=True)
    ventajas_tecnicas = models.JSONField(default=list, blank=True)
    imagen_principal = models.ImageField(upload_to='patentes/', blank=True, null=True, help_text="Imagen principal subida al servidor (recomendado: JPG, PNG)")
    imagen_principal_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen principal (alternativa)")
    documento_patente = models.FileField(upload_to='patentes/documentos/', blank=True, null=True, help_text="Documento de la patente subido al servidor (PDF recomendado)")
    documento_patente_url = models.URLField(blank=True, null=True, help_text="URL externa del documento de la patente (alternativa)")
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Patente"
        verbose_name_plural = "Patentes"
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('innovacion:patente_detail', kwargs={'slug': self.slug})

    def get_imagen_principal_url(self):
        """Retorna la URL de la imagen principal con prioridad para archivos subidos"""
        if self.imagen_principal:
            return self.imagen_principal.url
        elif self.imagen_principal_url:
            return self.imagen_principal_url
        return None

    def get_documento_patente_url(self):
        """Retorna la URL del documento de la patente con prioridad para archivos subidos"""
        if self.documento_patente:
            return self.documento_patente.url
        elif self.documento_patente_url:
            return self.documento_patente_url
        return None
