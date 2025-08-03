from django.contrib import admin
from .models import ProgramaSocial, Alianza, ImpactoAmbiental, ReporteSostenibilidad


@admin.register(ProgramaSocial)
class ProgramaSocialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'estado', 'destacado', 'orden']
    list_filter = ['categoria', 'estado', 'destacado']
    list_editable = ['estado', 'destacado', 'orden']
    search_fields = ['nombre', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('nombre',)}
    date_hierarchy = 'fecha_inicio'
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion_corta', 'descripcion_larga', 'categoria')
        }),
        ('Ubicación y Fechas', {
            'fields': ('ubicacion', 'fecha_inicio', 'fecha_fin')
        }),
        ('Presupuesto y Beneficiarios', {
            'fields': ('presupuesto', 'moneda', 'beneficiarios_directos', 'beneficiarios_indirectos')
        }),
        ('Objetivos y Resultados', {
            'fields': ('objetivos', 'resultados', 'impacto_social')
        }),
        ('Multimedia', {
            'fields': ('imagen_principal', 'galeria_imagenes', 'video_url')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(Alianza)
class AlianzaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_alianza', 'organizacion', 'estado', 'destacado']
    list_filter = ['tipo_alianza', 'estado', 'destacado']
    list_editable = ['estado', 'destacado']
    search_fields = ['nombre', 'descripcion', 'organizacion']
    prepopulated_fields = {'slug': ('nombre',)}
    date_hierarchy = 'fecha_inicio'
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion', 'tipo_alianza', 'organizacion')
        }),
        ('Contacto', {
            'fields': ('contacto_principal', 'email_contacto', 'telefono_contacto')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
        ('Objetivos y Resultados', {
            'fields': ('objetivos', 'resultados')
        }),
        ('Multimedia', {
            'fields': ('logo_organizacion', 'imagen_principal')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(ImpactoAmbiental)
class ImpactoAmbientalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'estado', 'destacado', 'orden']
    list_filter = ['categoria', 'estado', 'destacado']
    list_editable = ['estado', 'destacado', 'orden']
    search_fields = ['nombre', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('nombre',)}
    date_hierarchy = 'fecha_inicio'
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion_corta', 'descripcion_larga', 'categoria')
        }),
        ('Ubicación y Fechas', {
            'fields': ('ubicacion', 'fecha_inicio', 'fecha_fin')
        }),
        ('Presupuesto y Métricas', {
            'fields': ('presupuesto', 'moneda', 'hectareas_afectadas', 'especies_beneficiadas')
        }),
        ('Métricas Ambientales', {
            'fields': ('metricas_ambientales',)
        }),
        ('Objetivos y Resultados', {
            'fields': ('objetivos', 'resultados')
        }),
        ('Multimedia', {
            'fields': ('imagen_principal', 'galeria_imagenes', 'video_url')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(ReporteSostenibilidad)
class ReporteSostenibilidadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'año', 'tipo_reporte', 'estado', 'destacado']
    list_filter = ['año', 'tipo_reporte', 'estado', 'destacado']
    list_editable = ['estado', 'destacado']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_publicacion'
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'slug', 'descripcion', 'año', 'tipo_reporte')
        }),
        ('Contenido', {
            'fields': ('resumen_ejecutivo', 'indicadores_clave', 'logros_principales', 'desafios')
        }),
        ('Documentos', {
            'fields': ('archivo_pdf', 'imagen_portada')
        }),
        ('Publicación', {
            'fields': ('estado', 'fecha_publicacion')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('destacado', 'orden')
        }),
    )
