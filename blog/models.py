from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from core.models import Equipo
import re


class NoticiaBlog(models.Model):
    """Noticias y artículos del blog"""
    TIPO_CHOICES = [
        ('noticia', 'Noticia'),
        ('articulo', 'Artículo'),
        ('comunicado', 'Comunicado'),
        ('blog', 'Blog'),
    ]
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    slug = models.SlugField(max_length=255, unique=True)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=500, blank=True, null=True)
    contenido = models.TextField()
    resumen = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='noticia')
    categoria = models.ForeignKey('CategoriaBlog', on_delete=models.SET_NULL, blank=True, null=True, related_name='noticias')
    etiquetas = models.JSONField(default=list, blank=True)
    autor = models.ForeignKey(Equipo, on_delete=models.SET_NULL, blank=True, null=True)
    imagen_principal = models.ImageField(upload_to='blog/noticias/', blank=True, null=True, help_text="Imagen principal del artículo (recomendado: JPG, PNG)")
    imagen_principal_url = models.URLField(blank=True, null=True, help_text="URL externa de la imagen principal (alternativa)")
    galeria_imagenes = models.JSONField(default=list, blank=True, help_text="URLs de imágenes de la galería")
    video_url = models.URLField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='borrador')
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fecha_expiracion = models.DateTimeField(blank=True, null=True)
    vistas = models.IntegerField(default=0)
    destacado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Noticia/Blog"
        verbose_name_plural = "Noticias y Blog"
        ordering = ['-fecha_publicacion', 'titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:noticia_detail', kwargs={'slug': self.slug})

    def get_imagen_principal_url(self):
        """Retorna la URL de la imagen principal con prioridad para archivos subidos"""
        if self.imagen_principal:
            return self.imagen_principal.url
        elif self.imagen_principal_url:
            return self.imagen_principal_url
        return None

    def get_youtube_embed_url(self):
        """
        Convierte URLs de YouTube a formato embed
        """
        if not self.video_url:
            return None
        
        # Patrones para diferentes formatos de URL de YouTube
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]+)',
            r'youtube\.com/watch\?.*v=([a-zA-Z0-9_-]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.video_url)
            if match:
                video_id = match.group(1)
                return f'https://www.youtube.com/embed/{video_id}'
        
        # Si no coincide con ningún patrón, devolver la URL original
        return self.video_url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        if self.estado == 'publicado' and not self.fecha_publicacion:
            self.fecha_publicacion = timezone.now()
        super().save(*args, **kwargs)


class CategoriaBlog(models.Model):
    """Categorías del blog"""
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    orden = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría del Blog"
        verbose_name_plural = "Categorías del Blog"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
