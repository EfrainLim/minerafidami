from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Servicio(models.Model):
    """Servicios de la empresa minera"""
    slug = models.SlugField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion_corta = models.TextField(blank=True, null=True)
    descripcion_larga = models.TextField(blank=True, null=True)
    icono = models.CharField(max_length=255, blank=True, null=True)
    imagen_principal = models.URLField(blank=True, null=True)
    galeria_imagenes = models.JSONField(default=list, blank=True)
    caracteristicas = models.JSONField(default=list, blank=True)
    beneficios = models.JSONField(default=list, blank=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    destacado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('servicios:servicio_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class CategoriaServicio(models.Model):
    """Categorías de servicios"""
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría de Servicio"
        verbose_name_plural = "Categorías de Servicios"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre
