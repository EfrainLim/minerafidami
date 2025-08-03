from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import ConfiguracionGeneral, Pagina, Testimonio, Equipo, CertificacionPremio, RedSocial, HeroSection, Mensaje
from servicios.models import Servicio
from proyectos.models import Proyecto
from blog.models import NoticiaBlog
from innovacion.models import Tecnologia, Patente
from rsocial.models import ProgramaSocial, Alianza, ImpactoAmbiental, ReporteSostenibilidad
from carreras.models import Vacante
import time


class HomeView(TemplateView):
    """Vista para la página de inicio"""
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener configuración general
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener todos los hero sections activos para rotación automática
        try:
            heroes_activos = list(HeroSection.objects.filter(activo=True).order_by('orden'))
            if heroes_activos:
                # Para compatibilidad, mantener el hero_section actual
                current_time = int(time.time())
                rotation_interval = 30
                current_index = (current_time // rotation_interval) % len(heroes_activos)
                hero_section = heroes_activos[current_index]
            else:
                hero_section = None
                heroes_activos = []
        except:
            hero_section = None
            heroes_activos = []
        
        # Obtener mensajes activos
        try:
            mensajes = Mensaje.objects.filter(activo=True).order_by('orden')
            mensajes_activos = [m for m in mensajes if m.esta_activo()]
        except:
            mensajes_activos = []
        
        # Obtener redes sociales activas
        redes_sociales = RedSocial.objects.filter(activo=True).order_by('orden')
        
        # Obtener servicios destacados
        servicios_destacados = Servicio.objects.filter(
            estado='activo', 
            destacado=True
        ).order_by('orden')[:6]
        
        # Obtener proyectos destacados
        proyectos_destacados = Proyecto.objects.filter(
            estado='activo', 
            destacado=True
        ).order_by('-fecha_inicio')[:6]
        
        # Obtener noticias recientes
        noticias_recientes = NoticiaBlog.objects.filter(
            estado='publicado'
        ).order_by('-fecha_publicacion')[:3]
        
        # Obtener testimonios
        testimonios = Testimonio.objects.filter(
            estado='activo'
        ).order_by('orden')[:6]
        
        # Obtener equipo directivo
        equipo_directivo = Equipo.objects.filter(
            estado='activo',
            directivo=True
        ).order_by('orden')[:4]
        
        # Obtener tecnologías destacadas para sección de innovación
        try:
            tecnologias_destacadas = Tecnologia.objects.filter(
                estado='activo',
                destacada=True
            ).order_by('orden')[:3]
        except:
            tecnologias_destacadas = []
        
        # Obtener patentes destacadas
        try:
            patentes_destacadas = Patente.objects.filter(
                estado='activo',
                destacada=True
            ).order_by('orden')[:3]
        except:
            patentes_destacadas = []
        
        # Obtener programas sociales destacados
        try:
            programas_sociales = ProgramaSocial.objects.filter(
                estado='activo',
                destacado=True
            ).order_by('orden')[:4]
        except:
            programas_sociales = []
        
        # Obtener alianzas estratégicas destacadas
        try:
            alianzas_destacadas = Alianza.objects.filter(
                estado='activa',
                destacado=True
            ).order_by('orden')[:4]
        except:
            alianzas_destacadas = []
        
        # Obtener vacantes destacadas
        try:
            vacantes_destacadas = Vacante.objects.filter(
                estado='abierta',
                destacada=True
            ).order_by('-created_at')[:3]
        except:
            vacantes_destacadas = []
        
        # Obtener certificaciones destacadas
        try:
            certificaciones_destacadas = CertificacionPremio.objects.filter(
                estado='activo',
                destacada=True
            ).order_by('orden')[:4]
        except:
            certificaciones_destacadas = []
        
        context.update({
            'config': config,
            'hero_section': hero_section,
            'heroes_activos': heroes_activos,  # Todos los hero sections para JavaScript
            'mensajes': mensajes_activos,
            'redes_sociales': redes_sociales,
            'servicios_destacados': servicios_destacados,
            'proyectos_destacados': proyectos_destacados,
            'noticias_recientes': noticias_recientes,
            'testimonios': testimonios,
            'equipo_directivo': equipo_directivo,
            'tecnologias_destacadas': tecnologias_destacadas,
            'patentes_destacadas': patentes_destacadas,
            'programas_sociales': programas_sociales,
            'alianzas_destacadas': alianzas_destacadas,
            'vacantes_destacadas': vacantes_destacadas,
            'certificaciones_destacadas': certificaciones_destacadas,
        })
        
        return context


class PaginaDetailView(DetailView):
    """Vista para páginas estáticas"""
    model = Pagina
    template_name = 'core/pagina_detail.html'
    context_object_name = 'pagina'

    def get_queryset(self):
        return Pagina.objects.filter(estado='activo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        redes_sociales = RedSocial.objects.filter(activo=True).order_by('orden')
        context['redes_sociales'] = redes_sociales
        return context


class SobreNosotrosView(TemplateView):
    """Vista para la página Sobre Nosotros"""
    template_name = 'core/sobre_nosotros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            config = ConfiguracionGeneral.objects.first()
        except:
            config = None
        
        # Obtener redes sociales activas
        redes_sociales = RedSocial.objects.filter(activo=True).order_by('orden')
        
        # Obtener solo los 4 miembros principales (directivos y primeros en orden)
        equipo_principal = Equipo.objects.filter(
            estado='activo'
        ).order_by('orden')[:4]
        
        certificaciones = CertificacionPremio.objects.filter(
            estado='activo'
        ).order_by('orden')
        
        context.update({
            'config': config,
            'redes_sociales': redes_sociales,
            'equipo_principal': equipo_principal,
            'certificaciones': certificaciones,
        })
        
        return context


class EquipoListView(ListView):
    """Vista para listar todo el equipo"""
    model = Equipo
    template_name = 'core/equipo_list.html'
    context_object_name = 'equipo_list'
    paginate_by = 8  # Mostrar 8 miembros por página

    def get_queryset(self):
        queryset = Equipo.objects.filter(estado='activo').order_by('orden')
        
        # Filtrar por departamento si se especifica
        departamento = self.request.GET.get('departamento')
        if departamento and departamento != 'todos':
            queryset = queryset.filter(departamento__iexact=departamento)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener redes sociales activas
        redes_sociales = RedSocial.objects.filter(activo=True).order_by('orden')
        
        # Obtener departamentos únicos para filtros
        departamentos = Equipo.objects.filter(
            estado='activo',
            departamento__isnull=False
        ).exclude(
            departamento=''
        ).values_list('departamento', flat=True).distinct().order_by('departamento')
        
        # Obtener el departamento actual seleccionado
        departamento_actual = self.request.GET.get('departamento', 'todos')
        
        context.update({
            'redes_sociales': redes_sociales,
            'departamentos': departamentos,
            'departamento_actual': departamento_actual,
        })
        
        return context


class EquipoDetailView(DetailView):
    """Vista para detalle de miembro del equipo"""
    model = Equipo
    template_name = 'core/equipo_detail.html'
    context_object_name = 'miembro'

    def get_queryset(self):
        return Equipo.objects.filter(estado='activo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        redes_sociales = RedSocial.objects.filter(activo=True).order_by('orden')
        context['redes_sociales'] = redes_sociales
        return context
