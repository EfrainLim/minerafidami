from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CategoriaProyecto(models.Model):
    """Categorías de proyectos"""
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría de Proyecto"
        verbose_name_plural = "Categorías de Proyectos"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    """Proyectos mineros de la empresa"""
    ESTADO_PROYECTO_CHOICES = [
        ('planificacion', 'Planificación'),
        ('en_curso', 'En Curso'),
        ('completado', 'Completado'),
        ('suspendido', 'Suspendido'),
    ]

    slug = models.SlugField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    estado_proyecto = models.CharField(max_length=20, choices=ESTADO_PROYECTO_CHOICES, default='en_curso')
    categoria = models.ForeignKey(CategoriaProyecto, on_delete=models.SET_NULL, blank=True, null=True, help_text="Categoría del proyecto")
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    coordenadas_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    coordenadas_lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin_estimada = models.DateField(blank=True, null=True)
    fecha_fin_real = models.DateField(blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=10, default='USD')
    imagen_principal = models.ImageField(upload_to='proyectos/', blank=True, null=True, help_text="Imagen principal subida al servidor (recomendado: JPG, PNG)")
    imagen_principal_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen principal (alternativa)")
    galeria_imagenes = models.JSONField(default=list, blank=True)
    video_url = models.URLField(blank=True, null=True)
    tecnologias_utilizadas = models.JSONField(default=list, blank=True)
    resultados = models.JSONField(default=list, blank=True)
    impacto_ambiental = models.TextField(blank=True, null=True)
    beneficios_comunidad = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    destacado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_inicio', 'nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('proyectos:proyecto_detail', kwargs={'slug': self.slug})

    def get_imagen_principal_url(self):
        """Retorna la URL de la imagen principal con prioridad para archivos subidos"""
        if self.imagen_principal:
            return self.imagen_principal.url
        elif self.imagen_principal_url:
            return self.imagen_principal_url
        return None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
