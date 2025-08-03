from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


class ProgramaSocial(models.Model):
    """Programas de responsabilidad social y desarrollo comunitario"""
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=[
        ('educacion', 'Educación'),
        ('salud', 'Salud'),
        ('infraestructura', 'Infraestructura'),
        ('empleo', 'Generación de Empleo'),
        ('medio_ambiente', 'Medio Ambiente'),
        ('cultura', 'Cultura'),
        ('deportes', 'Deportes'),
        ('seguridad', 'Seguridad'),
    ])
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=10, default='PEN')
    beneficiarios_directos = models.IntegerField(blank=True, null=True)
    beneficiarios_indirectos = models.IntegerField(blank=True, null=True)
    objetivos = models.JSONField(default=list, blank=True)
    resultados = models.JSONField(default=list, blank=True)
    impacto_social = models.TextField(blank=True, null=True)
    imagen_principal = models.URLField(blank=True, null=True)
    galeria_imagenes = models.JSONField(default=list, blank=True)
    video_url = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('finalizado', 'Finalizado'),
    ], default='activo')
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Programa Social"
        verbose_name_plural = "Programas Sociales"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('rsocial:programa_detail', kwargs={'slug': self.slug})


class Alianza(models.Model):
    """Alianzas estratégicas para programas sociales"""
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_alianza = models.CharField(max_length=100, choices=[
        ('gobierno', 'Gobierno'),
        ('ong', 'ONG'),
        ('universidad', 'Universidad'),
        ('empresa', 'Empresa Privada'),
        ('comunidad', 'Comunidad'),
        ('internacional', 'Organización Internacional'),
    ])
    organizacion = models.CharField(max_length=255)
    contacto_principal = models.CharField(max_length=255, blank=True, null=True)
    email_contacto = models.EmailField(blank=True, null=True)
    telefono_contacto = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    objetivos = models.JSONField(default=list, blank=True)
    resultados = models.JSONField(default=list, blank=True)
    logo_organizacion = models.URLField(blank=True, null=True)
    imagen_principal = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
        ('finalizada', 'Finalizada'),
    ], default='activa')
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alianza"
        verbose_name_plural = "Alianzas"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('rsocial:alianza_detail', kwargs={'slug': self.slug})


class ImpactoAmbiental(models.Model):
    """Programas de impacto ambiental y sostenibilidad"""
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=[
        ('reforestacion', 'Reforestación'),
        ('conservacion', 'Conservación'),
        ('energia_renovable', 'Energía Renovable'),
        ('gestion_residuos', 'Gestión de Residuos'),
        ('agua', 'Gestión del Agua'),
        ('biodiversidad', 'Biodiversidad'),
        ('educacion_ambiental', 'Educación Ambiental'),
    ])
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=10, default='PEN')
    hectareas_afectadas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    especies_beneficiadas = models.JSONField(default=list, blank=True)
    metricas_ambientales = models.JSONField(default=dict, blank=True)
    objetivos = models.JSONField(default=list, blank=True)
    resultados = models.JSONField(default=list, blank=True)
    imagen_principal = models.URLField(blank=True, null=True)
    galeria_imagenes = models.JSONField(default=list, blank=True)
    video_url = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('finalizado', 'Finalizado'),
    ], default='activo')
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Impacto Ambiental"
        verbose_name_plural = "Impactos Ambientales"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('rsocial:impacto_detail', kwargs={'slug': self.slug})


class ReporteSostenibilidad(models.Model):
    """Reportes de sostenibilidad y responsabilidad social"""
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    año = models.IntegerField()
    tipo_reporte = models.CharField(max_length=100, choices=[
        ('sostenibilidad', 'Reporte de Sostenibilidad'),
        ('responsabilidad_social', 'Reporte de Responsabilidad Social'),
        ('ambiental', 'Reporte Ambiental'),
        ('gri', 'Reporte GRI'),
        ('integrado', 'Reporte Integrado'),
    ])
    archivo_pdf = models.URLField(blank=True, null=True)
    resumen_ejecutivo = models.TextField(blank=True, null=True)
    indicadores_clave = models.JSONField(default=dict, blank=True)
    logros_principales = models.JSONField(default=list, blank=True)
    desafios = models.JSONField(default=list, blank=True)
    imagen_portada = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ], default='borrador')
    fecha_publicacion = models.DateField(blank=True, null=True)
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reporte de Sostenibilidad"
        verbose_name_plural = "Reportes de Sostenibilidad"
        ordering = ['-año', 'orden', 'titulo']

    def __str__(self):
        return f"{self.titulo} ({self.año})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('rsocial:reporte_detail', kwargs={'slug': self.slug})
