from django.contrib import admin
from .models import Tecnologia, ProyectoInnovacion, Patente


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'estado', 'destacado', 'orden']
    list_filter = ['categoria', 'estado', 'destacado']
    list_editable = ['estado', 'destacado', 'orden']
    search_fields = ['nombre', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('nombre',)}
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion_corta', 'descripcion_larga', 'categoria')
        }),
        ('Multimedia', {
            'fields': ('imagen_principal', 'imagen_principal_url', 'galeria_imagenes', 'video_url'),
            'description': 'Sube archivos al servidor o proporciona URLs externas. Los archivos del servidor tienen prioridad.'
        }),
        ('Detalles', {
            'fields': ('beneficios', 'aplicaciones', 'fecha_implementacion')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(ProyectoInnovacion)
class ProyectoInnovacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_proyecto', 'estado_proyecto', 'estado', 'destacado']
    list_filter = ['tipo_proyecto', 'estado_proyecto', 'estado', 'destacado']
    list_editable = ['estado', 'destacado', 'estado_proyecto']
    search_fields = ['nombre', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('nombre',)}
    date_hierarchy = 'fecha_inicio'
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion_corta', 'descripcion_larga')
        }),
        ('Tipo y Estado', {
            'fields': ('tipo_proyecto', 'estado_proyecto')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin_estimada', 'fecha_fin_real')
        }),
        ('Presupuesto', {
            'fields': ('presupuesto', 'moneda')
        }),
        ('Equipo y Tecnologías', {
            'fields': ('tecnologias_utilizadas', 'equipo_investigacion')
        }),
        ('Resultados', {
            'fields': ('resultados', 'impacto_esperado')
        }),
        ('Multimedia', {
            'fields': ('imagen_principal', 'imagen_principal_url', 'galeria_imagenes', 'video_url'),
            'description': 'Sube archivos al servidor o proporciona URLs externas. Los archivos del servidor tienen prioridad.'
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(Patente)
class PatenteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'estado', 'destacado', 'orden']
    list_filter = ['tipo', 'estado', 'destacado']
    list_editable = ['estado', 'destacado', 'orden']
    search_fields = ['titulo', 'descripcion', 'numero_patente']
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_solicitud'
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'slug', 'descripcion', 'numero_patente', 'tipo')
        }),
        ('Estado y Fechas', {
            'fields': ('estado', 'fecha_solicitud', 'fecha_aprobacion', 'fecha_expiracion')
        }),
        ('Detalles Técnicos', {
            'fields': ('inventores', 'aplicacion_industrial', 'ventajas_tecnicas')
        }),
        ('Documentos', {
            'fields': ('imagen_principal', 'imagen_principal_url', 'documento_patente', 'documento_patente_url'),
            'description': 'Sube archivos al servidor o proporciona URLs externas. Los archivos del servidor tienen prioridad.'
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('destacado', 'orden')
        }),
    )
