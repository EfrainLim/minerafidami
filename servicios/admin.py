from django.contrib import admin
from .models import Servicio, CategoriaServicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'destacado', 'orden']
    list_filter = ['estado', 'destacado']
    list_editable = ['estado', 'destacado', 'orden']
    search_fields = ['nombre', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('nombre',)}
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'descripcion_corta', 'descripcion_larga')
        }),
        ('Multimedia', {
            'fields': ('icono', 'imagen_principal', 'galeria_imagenes')
        }),
        ('Características', {
            'fields': ('caracteristicas', 'beneficios')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(CategoriaServicio)
class CategoriaServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'orden']
    list_filter = ['estado']
    list_editable = ['estado', 'orden']
    search_fields = ['nombre', 'descripcion']
