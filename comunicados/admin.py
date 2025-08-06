from django.contrib import admin
from .models import CategoriaComunicado, Comunicado, ComunicadoVista


@admin.register(CategoriaComunicado)
class CategoriaComunicadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color', 'icono', 'orden', 'activo', 'created_at']
    list_filter = ['activo', 'created_at']
    list_editable = ['orden', 'activo']
    search_fields = ['nombre', 'descripcion']
    ordering = ['orden', 'nombre']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Apariencia', {
            'fields': ('color', 'icono')
        }),
        ('Configuración', {
            'fields': ('orden', 'activo')
        }),
    )


@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'prioridad', 'estado', 'mostrar_en_home', 'mostrar_en_popup', 'destacado', 'fecha_publicacion', 'vistas', 'descargas']
    list_filter = ['tipo', 'prioridad', 'estado', 'categoria', 'mostrar_en_home', 'mostrar_en_popup', 'destacado', 'fecha_publicacion', 'created_at']
    list_editable = ['estado', 'mostrar_en_home', 'mostrar_en_popup', 'destacado']
    search_fields = ['titulo', 'resumen', 'contenido', 'autor']
    date_hierarchy = 'fecha_publicacion'
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ['vistas', 'descargas', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'slug', 'resumen', 'contenido')
        }),
        ('Clasificación', {
            'fields': ('tipo', 'categoria', 'prioridad', 'estado', 'etiquetas')
        }),
        ('Configuración de Visualización', {
            'fields': ('mostrar_en_home', 'mostrar_en_popup', 'destacado')
        }),
        ('Programación', {
            'fields': ('fecha_publicacion', 'fecha_expiracion', 'activo'),
            'description': 'Configura cuándo se mostrará el comunicado'
        }),
        ('Metadatos', {
            'fields': ('autor', 'meta_title', 'meta_description')
        }),
        ('Archivos', {
            'fields': ('imagen_destacada', 'archivo_adjunto'),
            'classes': ('collapse',)
        }),
        ('Estadísticas', {
            'fields': ('vistas', 'descargas'),
            'classes': ('collapse',)
        }),
        ('Auditoría', {
            'fields': ('orden', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['marcar_como_publicado', 'marcar_como_archivado', 'activar_comunicados', 'desactivar_comunicados']
    
    def marcar_como_publicado(self, request, queryset):
        updated = queryset.update(estado='publicado')
        self.message_user(request, f'{updated} comunicado(s) marcado(s) como publicado(s).')
    marcar_como_publicado.short_description = "Marcar como publicado"
    
    def marcar_como_archivado(self, request, queryset):
        updated = queryset.update(estado='archivado')
        self.message_user(request, f'{updated} comunicado(s) marcado(s) como archivado(s).')
    marcar_como_archivado.short_description = "Marcar como archivado"
    
    def activar_comunicados(self, request, queryset):
        updated = queryset.update(activo=True)
        self.message_user(request, f'{updated} comunicado(s) activado(s).')
    activar_comunicados.short_description = "Activar comunicados"
    
    def desactivar_comunicados(self, request, queryset):
        updated = queryset.update(activo=False)
        self.message_user(request, f'{updated} comunicado(s) desactivado(s).')
    desactivar_comunicados.short_description = "Desactivar comunicados"


@admin.register(ComunicadoVista)
class ComunicadoVistaAdmin(admin.ModelAdmin):
    list_display = ['comunicado', 'ip_address', 'fecha_vista']
    list_filter = ['fecha_vista', 'comunicado']
    search_fields = ['comunicado__titulo', 'ip_address']
    date_hierarchy = 'fecha_vista'
    readonly_fields = ['comunicado', 'ip_address', 'user_agent', 'fecha_vista']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
