from django.db import models


class ImageFieldMixin:
    """
    Mixin para manejar campos de imagen con URL de respaldo.
    Reduce duplicación de código en modelos que tienen campos de imagen.
    """
    
    def get_image_url(self, field_name, url_field_name):
        """
        Obtener URL de imagen con prioridad para archivos subidos.
        
        Args:
            field_name (str): Nombre del campo ImageField
            url_field_name (str): Nombre del campo URLField
            
        Returns:
            str: URL de la imagen o None si no existe
        """
        image_field = getattr(self, field_name, None)
        url_field = getattr(self, url_field_name, None)
        
        if image_field:
            return image_field.url
        elif url_field:
            return url_field
        return None


class TimestampMixin:
    """
    Mixin para agregar campos de timestamp automáticos.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class StatusMixin:
    """
    Mixin para agregar campo de estado con opciones comunes.
    """
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='activo'
    )
    
    class Meta:
        abstract = True


class OrderMixin:
    """
    Mixin para agregar campo de orden para listas ordenadas.
    """
    orden = models.IntegerField(default=0)
    
    class Meta:
        abstract = True
        ordering = ['orden']


class SlugMixin:
    """
    Mixin para agregar campo slug con generación automática.
    """
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)
    
    def generate_slug(self):
        """
        Generar slug basado en el nombre del objeto.
        Debe ser implementado en las clases que heredan.
        """
        raise NotImplementedError("Subclases deben implementar generate_slug()") 