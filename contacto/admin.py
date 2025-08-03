from django.contrib import admin
from .models import Contacto, Newsletter


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'tipo_consulta', 'estado', 'fecha_contacto']
    list_filter = ['tipo_consulta', 'estado', 'fecha_contacto']
    list_editable = ['estado']
    search_fields = ['nombre', 'email', 'asunto', 'mensaje']
    date_hierarchy = 'fecha_contacto'
    readonly_fields = ['fecha_contacto']
    fieldsets = (
        ('Información de Contacto', {
            'fields': ('nombre', 'email', 'telefono', 'empresa', 'cargo')
        }),
        ('Consulta', {
            'fields': ('asunto', 'mensaje', 'tipo_consulta')
        }),
        ('Estado', {
            'fields': ('estado', 'respuesta', 'fecha_respuesta')
        }),
        ('Información del Sistema', {
            'fields': ('fecha_contacto',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'empresa', 'estado', 'fecha_suscripcion']
    list_filter = ['estado', 'fecha_suscripcion']
    list_editable = ['estado']
    search_fields = ['email', 'nombre', 'empresa']
    date_hierarchy = 'fecha_suscripcion'
    readonly_fields = ['fecha_suscripcion']
