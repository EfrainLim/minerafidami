from django.contrib import admin
from .models import NoticiaBlog, CategoriaBlog


@admin.register(NoticiaBlog)
class NoticiaBlogAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'categoria', 'autor', 'estado', 'fecha_publicacion', 'destacado']
    list_filter = ['tipo', 'estado', 'destacado', 'fecha_publicacion', 'categoria']
    list_editable = ['estado', 'destacado']
    search_fields = ['titulo', 'subtitulo', 'contenido', 'resumen']
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_publicacion'
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'subtitulo', 'slug', 'contenido', 'resumen')
        }),
        ('Clasificación', {
            'fields': ('tipo', 'categoria', 'etiquetas')
        }),
        ('Autor', {
            'fields': ('autor',)
        }),
        ('Multimedia', {
            'fields': ('imagen_principal', 'imagen_principal_url', 'galeria_imagenes', 'video_url'),
            'description': 'Los archivos subidos tienen prioridad sobre las URLs externas'
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Publicación', {
            'fields': ('estado', 'fecha_publicacion', 'fecha_expiracion', 'destacado')
        }),
        ('Estadísticas', {
            'fields': ('vistas',)
        }),
    )


@admin.register(CategoriaBlog)
class CategoriaBlogAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'orden']
    list_filter = ['estado']
    list_editable = ['estado', 'orden']
    search_fields = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'slug')
        }),
        ('Configuración', {
            'fields': ('orden', 'estado')
        }),
    )
