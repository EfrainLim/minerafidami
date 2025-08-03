from django.contrib import admin
from .models import Proyecto, CategoriaProyecto


@admin.register(CategoriaProyecto)
class CategoriaProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden', 'estado', 'created_at']
    list_filter = ['estado', 'created_at']
    list_editable = ['orden', 'estado']
    search_fields = ['nombre', 'descripcion']
    ordering = ['orden', 'nombre']


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'estado_proyecto', 'ubicacion', 'fecha_inicio', 'estado', 'destacado', 'orden']
    list_filter = ['estado_proyecto', 'estado', 'destacado', 'categoria', 'fecha_inicio']
    list_editable = ['estado', 'destacado', 'orden']
    search_fields = ['nombre', 'descripcion_corta', 'descripcion_larga', 'ubicacion']
    prepopulated_fields = {'slug': ('nombre',)}
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-fecha_inicio', 'nombre']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion_corta', 'descripcion_larga')
        }),
        ('Estado y Categoría', {
            'fields': ('estado_proyecto', 'categoria')
        }),
        ('Ubicación', {
            'fields': ('ubicacion', 'coordenadas_lat', 'coordenadas_lng')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin_estimada', 'fecha_fin_real')
        }),
        ('Presupuesto', {
            'fields': ('presupuesto', 'moneda')
        }),
        ('Multimedia', {
            'fields': ('imagen_principal', 'imagen_principal_url', 'galeria_imagenes', 'video_url'),
            'description': 'Sube archivos al servidor o proporciona URLs externas. Los archivos del servidor tienen prioridad.'
        }),
        ('Tecnologías y Resultados', {
            'fields': ('tecnologias_utilizadas', 'resultados')
        }),
        ('Impacto y Beneficios', {
            'fields': ('impacto_ambiental', 'beneficios_comunidad')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('orden', 'estado', 'destacado')
        }),
        ('Información del Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
