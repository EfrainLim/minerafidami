from django.contrib import admin
from .models import Vacante, Postulacion


@admin.register(Vacante)
class VacanteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo_contrato', 'ubicacion', 'departamento', 'estado', 'destacada', 'postulaciones']
    list_filter = ['tipo_contrato', 'estado', 'destacada', 'departamento']
    list_editable = ['estado', 'destacada']
    search_fields = ['titulo', 'descripcion', 'ubicacion']
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'slug', 'descripcion')
        }),
        ('Requisitos y Responsabilidades', {
            'fields': ('requisitos', 'responsabilidades', 'beneficios')
        }),
        ('Detalles del Puesto', {
            'fields': ('tipo_contrato', 'ubicacion', 'departamento', 'experiencia_minima', 'experiencia_maxima')
        }),
        ('Salario', {
            'fields': ('salario_min', 'salario_max', 'moneda')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacada', 'fecha_limite')
        }),
        ('Estadísticas', {
            'fields': ('vistas', 'postulaciones')
        }),
    )


@admin.register(Postulacion)
class PostulacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'vacante', 'email', 'estado', 'fecha_postulacion']
    list_filter = ['estado', 'fecha_postulacion', 'vacante']
    list_editable = ['estado']
    search_fields = ['nombre', 'apellido', 'email', 'vacante__titulo']
    date_hierarchy = 'fecha_postulacion'
    fieldsets = (
        ('Información Personal', {
            'fields': ('vacante', 'nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'nacionalidad')
        }),
        ('Experiencia y Educación', {
            'fields': ('experiencia_anos', 'educacion', 'cv_url')
        }),
        ('Documentos', {
            'fields': ('carta_motivacion', 'referencias')
        }),
        ('Estado', {
            'fields': ('estado', 'notas_internas', 'fecha_revision')
        }),
    )
