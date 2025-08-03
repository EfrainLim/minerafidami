from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
import os
from .models import ConfiguracionGeneral, Equipo, Testimonio, CertificacionPremio, HeroSection
from blog.models import NoticiaBlog
from innovacion.models import Patente, Tecnologia, ProyectoInnovacion
from proyectos.models import Proyecto


def eliminar_archivo_anterior_generico(sender, instance, campos_imagen, **kwargs):
    """
    Señal genérica para eliminar archivos anteriores cuando se actualizan imágenes
    campos_imagen: lista de nombres de campos de imagen a verificar
    """
    if instance.pk:
        try:
            instancia_anterior = sender.objects.get(pk=instance.pk)
            
            for campo in campos_imagen:
                campo_anterior = getattr(instancia_anterior, campo, None)
                campo_actual = getattr(instance, campo, None)
                
                # Verificar si el campo cambió o se eliminó
                if campo_anterior and (not campo_actual or campo_anterior != campo_actual):
                    if hasattr(campo_anterior, 'path') and os.path.isfile(campo_anterior.path):
                        os.remove(campo_anterior.path)
                        print(f"✅ Archivo anterior eliminado: {campo_anterior.path}")
                        
        except sender.DoesNotExist:
            pass


def eliminar_archivos_al_eliminar_generico(sender, instance, campos_imagen, **kwargs):
    """
    Señal genérica para eliminar archivos cuando se elimina una instancia
    campos_imagen: lista de nombres de campos de imagen a verificar
    """
    for campo in campos_imagen:
        archivo = getattr(instance, campo, None)
        if archivo and hasattr(archivo, 'path') and os.path.isfile(archivo.path):
            os.remove(archivo.path)
            print(f"✅ Archivo eliminado: {archivo.path}")


# Configuración de campos de imagen por modelo
CAMPOS_IMAGEN_CONFIG = {
    ConfiguracionGeneral: ['logo', 'favicon'],
    Equipo: ['foto'],  # Actualizado para usar el nuevo campo foto
    Testimonio: ['imagen'],
    CertificacionPremio: ['url_logo', 'url_documento'],
    NoticiaBlog: ['imagen_principal'],
    HeroSection: ['imagen_fondo'],
    Patente: ['imagen_principal', 'documento_patente'],
    Tecnologia: ['imagen_principal'],
    ProyectoInnovacion: ['imagen_principal'],
    Proyecto: ['imagen_principal'],
}


# Registrar señales para todos los modelos
for modelo, campos in CAMPOS_IMAGEN_CONFIG.items():
    # Señal pre_save para eliminar archivos anteriores
    pre_save.connect(
        lambda sender, instance, **kwargs: eliminar_archivo_anterior_generico(
            sender, instance, CAMPOS_IMAGEN_CONFIG[sender], **kwargs
        ),
        sender=modelo
    )
    
    # Señal post_delete para eliminar archivos al eliminar instancia
    post_delete.connect(
        lambda sender, instance, **kwargs: eliminar_archivos_al_eliminar_generico(
            sender, instance, CAMPOS_IMAGEN_CONFIG[sender], **kwargs
        ),
        sender=modelo
    ) 