from django.db import models


class Contacto(models.Model):
    """Formularios de contacto"""
    TIPO_CONSULTA_CHOICES = [
        ('general', 'General'),
        ('cotizacion', 'Cotización'),
        ('trabajo', 'Trabajo'),
        ('prensa', 'Prensa'),
        ('inversion', 'Inversión'),
    ]
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('en_revision', 'En Revisión'),
        ('respondido', 'Respondido'),
        ('archivado', 'Archivado'),
    ]

    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    asunto = models.CharField(max_length=255, blank=True, null=True)
    mensaje = models.TextField()
    tipo_consulta = models.CharField(max_length=20, choices=TIPO_CONSULTA_CHOICES, default='general')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nuevo')
    respuesta = models.TextField(blank=True, null=True)
    fecha_contacto = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-fecha_contacto']

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"


class Newsletter(models.Model):
    """Suscriptores del newsletter"""
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('baja', 'Baja'),
    ]

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    intereses = models.JSONField(default=list, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    fecha_suscripcion = models.DateTimeField(auto_now_add=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Suscriptor Newsletter"
        verbose_name_plural = "Suscriptores Newsletter"
        ordering = ['-fecha_suscripcion']

    def __str__(self):
        return self.email
