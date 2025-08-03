from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Vacante(models.Model):
    """Ofertas de trabajo"""
    TIPO_CONTRATO_CHOICES = [
        ('tiempo_completo', 'Tiempo Completo'),
        ('tiempo_parcial', 'Tiempo Parcial'),
        ('contrato', 'Contrato'),
        ('practicas', 'Prácticas'),
    ]

    slug = models.SlugField(max_length=255, unique=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    requisitos = models.JSONField(default=list, blank=True)
    responsabilidades = models.JSONField(default=list, blank=True)
    beneficios = models.JSONField(default=list, blank=True)
    tipo_contrato = models.CharField(max_length=20, choices=TIPO_CONTRATO_CHOICES)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    experiencia_minima = models.IntegerField(blank=True, null=True)
    experiencia_maxima = models.IntegerField(blank=True, null=True)
    salario_min = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salario_max = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=10, default='USD')
    fecha_limite = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada'), ('suspendida', 'Suspendida')], default='abierta')
    destacada = models.BooleanField(default=False)
    vistas = models.IntegerField(default=0)
    postulaciones = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vacante"
        verbose_name_plural = "Vacantes"
        ordering = ['-created_at', 'titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('carreras:vacante_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Postulacion(models.Model):
    """Postulaciones a vacantes"""
    ESTADO_CHOICES = [
        ('recibida', 'Recibida'),
        ('revisando', 'Revisando'),
        ('entrevista', 'Entrevista'),
        ('rechazada', 'Rechazada'),
        ('contratada', 'Contratada'),
    ]

    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    experiencia_anos = models.IntegerField(blank=True, null=True)
    educacion = models.TextField(blank=True, null=True)
    cv_url = models.URLField(blank=True, null=True)
    carta_motivacion = models.TextField(blank=True, null=True)
    referencias = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='recibida')
    notas_internas = models.TextField(blank=True, null=True)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    fecha_revision = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"
        ordering = ['-fecha_postulacion']

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.vacante.titulo}"
