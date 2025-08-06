from django.contrib import admin
from .models import ConfiguracionGeneral, Testimonio, Equipo, CertificacionPremio, RedSocial, HeroSection


@admin.register(ConfiguracionGeneral)
class ConfiguracionGeneralAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa', 'email_contacto', 'telefono_principal', 'updated_at']
    list_editable = ['email_contacto', 'telefono_principal']
    fieldsets = (
        ('Información General', {
            'fields': ('nombre_empresa', 'slogan', 'descripcion_corta', 'descripcion_larga')
        }),
        ('Misión y Visión', {
            'fields': ('mision', 'vision', 'valores')
        }),
        ('Contacto', {
            'fields': ('email_contacto', 'telefono_principal', 'direccion_oficina', 'horario_atencion')
        }),
        ('Ubicación', {
            'fields': ('coordenadas_lat', 'coordenadas_lng')
        }),
        ('Multimedia', {
            'fields': ('logo', 'logo_url', 'favicon', 'favicon_url'),
            'description': 'Los archivos subidos tienen prioridad sobre las URLs externas'
        }),
        ('SEO', {
            'fields': ('meta_title_default', 'meta_description_default', 'meta_keywords_default')
        }),
        ('Analytics', {
            'fields': ('google_analytics_id', 'facebook_pixel_id')
        }),
    )





@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'empresa', 'cargo', 'calificacion', 'destacado', 'estado', 'orden']
    list_filter = ['estado', 'destacado', 'calificacion']
    list_editable = ['destacado', 'estado', 'orden', 'calificacion']
    search_fields = ['nombre', 'empresa', 'testimonio']
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'cargo', 'empresa')
        }),
        ('Testimonio', {
            'fields': ('testimonio', 'calificacion', 'proyecto_relacionado')
        }),
        ('Multimedia', {
            'fields': ('imagen', 'imagen_url'),
            'description': 'Sube una imagen al servidor o proporciona una URL externa. La imagen del servidor tiene prioridad.'
        }),
        ('Configuración', {
            'fields': ('estado', 'destacado', 'orden')
        }),
    )


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cargo', 'departamento', 'directivo', 'estado', 'orden']
    list_filter = ['estado', 'directivo', 'departamento']
    list_editable = ['cargo', 'departamento', 'directivo', 'estado', 'orden']
    search_fields = ['nombre', 'apellido', 'cargo', 'biografia']
    prepopulated_fields = {'slug': ('nombre', 'apellido')}
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'slug', 'cargo', 'departamento', 'biografia')
        }),
        ('Foto', {
            'fields': ('foto', 'foto_url'),
            'description': 'Los archivos subidos tienen prioridad sobre las URLs externas'
        }),
        ('Experiencia y Educación', {
            'fields': ('experiencia_anos', 'especialidades', 'educacion', 'certificaciones')
        }),
        ('Contacto', {
            'fields': ('email', 'linkedin_url')
        }),
        ('Configuración', {
            'fields': ('estado', 'directivo', 'orden')
        }),
    )


@admin.register(CertificacionPremio)
class CertificacionPremioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'categoria', 'organismo_otorgante', 'estado', 'orden']
    list_filter = ['tipo', 'estado', 'categoria']
    list_editable = ['estado', 'orden']
    search_fields = ['nombre', 'descripcion', 'organismo_otorgante']
    prepopulated_fields = {'slug': ('nombre',)}
    date_hierarchy = 'fecha_otorgamiento'
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'tipo', 'categoria', 'descripcion')
        }),
        ('Organismo y Fechas', {
            'fields': ('organismo_otorgante', 'fecha_otorgamiento', 'fecha_vencimiento')
        }),
        ('Archivos', {
            'fields': ('url_logo', 'url_documento'),
            'description': 'URLs de los archivos de la certificación'
        }),
        ('Configuración', {
            'fields': ('estado', 'orden')
        }),
    )


@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'url', 'activo', 'orden', 'color_preview']
    list_filter = ['activo', 'nombre']
    list_editable = ['activo', 'orden']
    search_fields = ['nombre', 'url']
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'url', 'activo', 'orden')
        }),
        ('Personalización', {
            'fields': ('icono', 'color'),
            'description': 'Deja vacío para usar los valores por defecto'
        }),
    )

    def color_preview(self, obj):
        if obj.get_color():
            return f'<div style="background-color: {obj.get_color()}; width: 20px; height: 20px; border-radius: 50%;"></div>'
        return '-'
    color_preview.short_description = 'Color'
    color_preview.allow_tags = True


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'orden', 'activo', 'updated_at']
    list_filter = ['activo']
    list_editable = ['orden', 'activo']
    search_fields = ['titulo_principal', 'subtitulo']
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo_principal', 'subtitulo')
        }),
        ('Imagen de Fondo', {
            'fields': ('imagen_fondo', 'imagen_fondo_url'),
            'description': 'Los archivos subidos tienen prioridad sobre las URLs externas'
        }),
        ('Botones', {
            'fields': ('texto_boton_principal', 'url_boton_principal', 'texto_boton_secundario', 'url_boton_secundario')
        }),
        ('Configuración', {
            'fields': ('activo', 'orden')
        }),
    )



