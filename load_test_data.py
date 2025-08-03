#!/usr/bin/env python
import os
import sys
import django
from datetime import date, timedelta
import random

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minerafidami.settings')
django.setup()

from core.models import ConfiguracionGeneral, Pagina, Testimonio, Equipo, CertificacionPremio, RedSocial, HeroSection, Mensaje
from servicios.models import Servicio, CategoriaServicio
from proyectos.models import Proyecto, CategoriaProyecto
from innovacion.models import Tecnologia, ProyectoInnovacion, Patente
from rsocial.models import ProgramaSocial, Alianza, ImpactoAmbiental, ReporteSostenibilidad
from blog.models import NoticiaBlog, CategoriaBlog
from carreras.models import Vacante, Postulacion
from contacto.models import Contacto, Newsletter

def limpiar_datos_existentes():
    """Limpiar todos los datos existentes"""
    print("🧹 Limpiando datos existentes...")
    
    # Limpiar en orden inverso para evitar problemas de dependencias
    Contacto.objects.all().delete()
    Newsletter.objects.all().delete()
    Postulacion.objects.all().delete()
    Vacante.objects.all().delete()
    NoticiaBlog.objects.all().delete()
    CategoriaBlog.objects.all().delete()
    ReporteSostenibilidad.objects.all().delete()
    ImpactoAmbiental.objects.all().delete()
    Alianza.objects.all().delete()
    ProgramaSocial.objects.all().delete()
    Patente.objects.all().delete()
    ProyectoInnovacion.objects.all().delete()
    Tecnologia.objects.all().delete()
    Proyecto.objects.all().delete()
    CategoriaProyecto.objects.all().delete()
    Servicio.objects.all().delete()
    CategoriaServicio.objects.all().delete()
    Mensaje.objects.all().delete()
    HeroSection.objects.all().delete()
    RedSocial.objects.all().delete()
    CertificacionPremio.objects.all().delete()
    Testimonio.objects.all().delete()
    Equipo.objects.all().delete()
    Pagina.objects.all().delete()
    ConfiguracionGeneral.objects.all().delete()
    
    print("✅ Datos existentes eliminados")

def crear_datos_prueba():
    """Crear datos de prueba para todas las tablas"""
    
    print("🚀 Iniciando carga de datos de prueba...")
    
    # Limpiar datos existentes primero
    limpiar_datos_existentes()
    
    # 1. Configuración General
    print("📋 Creando configuración general...")
    config_data = {
        'nombre_empresa': 'Minera Fidami S.A.',
        'slogan': 'Líderes en Minería Subterránea Sostenible',
        'descripcion_corta': 'Empresa minera especializada en extracción de oro mediante minería subterránea en Sancos, Lucanas, Ayacucho.',
        'descripcion_larga': 'Minera Fidami S.A. es una empresa minera peruana especializada en la extracción de oro mediante técnicas de minería subterránea. Nuestras operaciones se centran en el proyecto Rampa Nueva Jerusalén, ubicado en el distrito de Sancos, provincia de Lucanas, departamento de Ayacucho. Operamos con los más altos estándares de seguridad, protección ambiental y responsabilidad social.',
        'mision': 'Extraer oro de manera sostenible y responsable, contribuyendo al desarrollo económico de la región de Ayacucho mientras protegemos el medio ambiente y promovemos el bienestar de nuestras comunidades vecinas.',
        'vision': 'Ser reconocidos como líderes en minería subterránea sostenible, innovadores en tecnología minera y referentes en responsabilidad social y ambiental en el Perú.',
        'valores': ['Seguridad', 'Sostenibilidad', 'Innovación', 'Responsabilidad Social', 'Excelencia Operacional', 'Integridad'],
        'email_contacto': 'recepcion@minerafidami.com.pe',
        'telefono_principal': '+51 914599576',
        'direccion_oficina': 'Sancos, Lucanas, Ayacucho, Perú',
        'coordenadas_lat': -14.4833,
        'coordenadas_lng': -74.6167,
        'horario_atencion': 'Lunes a Viernes: 8:00 AM - 6:00 PM',
        'meta_title_default': 'Minera Fidami S.A. - Minería Subterránea de Oro en Sancos, Ayacucho',
        'meta_description_default': 'Minera Fidami S.A. es una empresa minera especializada en extracción de oro mediante minería subterránea en Sancos, Lucanas, Ayacucho. Proyecto Rampa Nueva Jerusalén.',
        'meta_keywords_default': 'minería subterránea, oro, Sancos, Ayacucho, Minera Fidami, Rampa Nueva Jerusalén, minería sostenible',
        'google_analytics_id': 'G-XXXXXXXXXX'
    }
    
    ConfiguracionGeneral.objects.create(**config_data)
    
    # 2. Categorías de Servicios
    print("🔧 Creando categorías de servicios...")
    categorias_servicios_data = [
        {
            'nombre': 'Extracción Subterránea',
            'descripcion': 'Servicios especializados en extracción de minerales mediante minería subterránea',
            'icono': 'fas fa-mountain',
            'orden': 1
        },
        {
            'nombre': 'Procesamiento de Minerales',
            'descripcion': 'Servicios de procesamiento y beneficio de minerales auríferos',
            'icono': 'fas fa-industry',
            'orden': 2
        },
        {
            'nombre': 'Infraestructura Minera',
            'descripcion': 'Desarrollo de infraestructura subterránea y de soporte',
            'icono': 'fas fa-road',
            'orden': 3
        },
        {
            'nombre': 'Gestión Ambiental',
            'descripcion': 'Servicios de manejo ambiental y cumplimiento normativo',
            'icono': 'fas fa-leaf',
            'orden': 4
        },
        {
            'nombre': 'Logística y Exportación',
            'descripcion': 'Servicios logísticos y de exportación de minerales',
            'icono': 'fas fa-ship',
            'orden': 5
        }
    ]
    
    for cat_data in categorias_servicios_data:
        CategoriaServicio.objects.create(**cat_data)
    
    # 3. Servicios
    print("⚙️ Creando servicios...")
    servicios_data = [
        {
            'nombre': 'Extracción de Oro Subterránea',
            'slug': 'extraccion-oro-subterranea',
            'descripcion_corta': 'Servicios especializados en extracción de oro mediante técnicas de minería subterránea avanzadas.',
            'descripcion_larga': 'Ofrecemos servicios completos de extracción de oro subterránea incluyendo perforación, voladura, carguío y acarreo de mineral aurífero. Nuestro equipo utiliza tecnología de punta y métodos de explotación optimizados para maximizar la recuperación de oro mientras garantizamos la seguridad operacional.',
            'caracteristicas': [
                'Perforación y voladura controlada',
                'Sistema de ventilación subterránea',
                'Control de estabilidad de taludes',
                'Monitoreo de gases y calidad del aire',
                'Equipos de carguío y acarreo especializados',
                'Sistema de drenaje subterráneo'
            ],
            'beneficios': [
                'Máxima recuperación de oro',
                'Seguridad operacional garantizada',
                'Cumplimiento de estándares ambientales',
                'Optimización de costos operativos',
                'Reducción de impacto ambiental',
                'Tecnología de punta en extracción'
            ],
            'icono': 'fas fa-mountain',
            'orden': 1
        },
        {
            'nombre': 'Procesamiento de Minerales',
            'slug': 'procesamiento-minerales',
            'descripcion_corta': 'Planta de procesamiento de minerales con capacidad para tratar mineral aurífero de alta ley.',
            'descripcion_larga': 'Nuestra planta de procesamiento de minerales está diseñada para el tratamiento eficiente de mineral aurífero. El proceso incluye chancado, molienda, flotación, cianuración y recuperación de oro por carbón activado, logrando una recuperación superior al 95%.',
            'caracteristicas': [
                'Chancado primario y secundario',
                'Molienda y clasificación',
                'Flotación de minerales auríferos',
                'Cianuración y lixiviación',
                'Recuperación de oro por carbón activado',
                'Control de calidad en línea'
            ],
            'beneficios': [
                'Alta recuperación de oro (95%+)',
                'Procesamiento de minerales complejos',
                'Automatización de procesos',
                'Cumplimiento de estándares internacionales',
                'Optimización energética',
                'Monitoreo continuo de calidad'
            ],
            'icono': 'fas fa-industry',
            'orden': 2
        },
        {
            'nombre': 'Desarrollo de Túneles y Rampas',
            'slug': 'desarrollo-tuneles-rampas',
            'descripcion_corta': 'Construcción y mantenimiento de infraestructura subterránea para el proyecto Rampa Nueva Jerusalén.',
            'descripcion_larga': 'Especialistas en el desarrollo de infraestructura subterránea incluyendo túneles, rampas, galerías y cámaras de explotación. Nuestro equipo cuenta con experiencia en el proyecto Rampa Nueva Jerusalén y utiliza técnicas modernas de sostenimiento y control geotécnico.',
            'caracteristicas': [
                'Diseño y construcción de rampas principales',
                'Desarrollo de galerías de acceso',
                'Construcción de cámaras de explotación',
                'Sistema de ventilación subterránea',
                'Sostenimiento con shotcrete y pernos',
                'Control geotécnico y monitoreo'
            ],
            'beneficios': [
                'Infraestructura subterránea segura',
                'Optimización del flujo de mineral',
                'Reducción de tiempos de transporte',
                'Cumplimiento de estándares de seguridad',
                'Diseño adaptado a condiciones geológicas',
                'Mantenimiento preventivo programado'
            ],
            'icono': 'fas fa-road',
            'orden': 3
        },
        {
            'nombre': 'Gestión de Residuos Mineros',
            'slug': 'gestion-residuos-mineros',
            'descripcion_corta': 'Manejo integral de relaves y residuos mineros con tecnologías modernas.',
            'descripcion_larga': 'Ofrecemos servicios integrales de gestión de residuos mineros incluyendo el diseño, construcción y operación de depósitos de relaves con las más altas tecnologías de impermeabilización y monitoreo ambiental.',
            'caracteristicas': [
                'Depósito de relaves con geomembrana',
                'Sistema de monitoreo de presas',
                'Tratamiento de aguas residuales',
                'Recuperación de agua de proceso',
                'Estabilización de relaves',
                'Monitoreo ambiental continuo'
            ],
            'beneficios': [
                'Cumplimiento ambiental total',
                'Reutilización de agua de proceso',
                'Estabilidad geotécnica garantizada',
                'Reducción de huella hídrica',
                'Monitoreo en tiempo real',
                'Certificación internacional'
            ],
            'icono': 'fas fa-recycle',
            'orden': 4
        },
        {
            'nombre': 'Logística y Exportación',
            'slug': 'logistica-exportacion',
            'descripcion_corta': 'Servicios logísticos completos para la exportación de concentrado de oro.',
            'descripcion_larga': 'Gestionamos todo el proceso logístico para la exportación de concentrado de oro a mercados internacionales, incluyendo transporte terrestre, almacenamiento portuario, documentación aduanera y certificación de calidad.',
            'caracteristicas': [
                'Transporte terrestre especializado',
                'Almacenamiento en puerto',
                'Documentación aduanera completa',
                'Certificación de calidad internacional',
                'Seguro de transporte marítimo',
                'Trazabilidad del producto'
            ],
            'beneficios': [
                'Cumplimiento de estándares internacionales',
                'Optimización de costos logísticos',
                'Trazabilidad completa del producto',
                'Reducción de tiempos de exportación',
                'Certificación de calidad garantizada',
                'Acceso a mercados premium'
            ],
            'icono': 'fas fa-ship',
            'orden': 5
        },
        {
            'nombre': 'Consultoría en Minería Subterránea',
            'slug': 'consultoria-mineria-subterranea',
            'descripcion_corta': 'Servicios de consultoría especializada en minería subterránea.',
            'descripcion_larga': 'Brindamos servicios de consultoría integral en minería subterránea, incluyendo estudios de factibilidad, optimización de procesos, planificación de minado y capacitación técnica especializada.',
            'caracteristicas': [
                'Estudios de factibilidad técnica',
                'Optimización de procesos mineros',
                'Planificación de minado',
                'Evaluación de reservas minerales',
                'Análisis de costos operativos',
                'Capacitación técnica especializada'
            ],
            'beneficios': [
                'Optimización de recursos mineros',
                'Reducción de costos operativos',
                'Mejora de productividad',
                'Transferencia de conocimiento',
                'Cumplimiento de mejores prácticas',
                'Innovación tecnológica continua'
            ],
            'icono': 'fas fa-chart-line',
            'orden': 6
        },
        {
            'nombre': 'Exploración Geológica',
            'slug': 'exploracion-geologica',
            'descripcion_corta': 'Servicios de exploración geológica y evaluación de recursos minerales.',
            'descripcion_larga': 'Realizamos exploración geológica integral para identificar nuevos yacimientos de oro en la región de Sancos, Lucanas, Ayacucho. Utilizamos técnicas avanzadas de prospección y evaluación de recursos.',
            'caracteristicas': [
                'Mapeo geológico detallado',
                'Perforación diamantina',
                'Análisis geoquímicos',
                'Modelamiento 3D de yacimientos',
                'Evaluación de reservas minerales',
                'Estudios de factibilidad económica'
            ],
            'beneficios': [
                'Identificación de nuevos yacimientos',
                'Evaluación precisa de recursos',
                'Reducción de riesgos exploratorios',
                'Optimización de inversiones',
                'Cumplimiento de estándares JORC/NI 43-101',
                'Desarrollo sostenible de recursos'
            ],
            'icono': 'fas fa-search',
            'orden': 7
        },
        {
            'nombre': 'Capacitación y Desarrollo',
            'slug': 'capacitacion-desarrollo',
            'descripcion_corta': 'Programas de capacitación especializada para personal minero.',
            'descripcion_larga': 'Ofrecemos programas de capacitación y desarrollo profesional para personal de la industria minera, con énfasis en seguridad, tecnología y mejores prácticas operacionales.',
            'caracteristicas': [
                'Capacitación en seguridad minera',
                'Entrenamiento en equipos especializados',
                'Desarrollo de competencias técnicas',
                'Programas de liderazgo',
                'Certificaciones profesionales',
                'Capacitación en nuevas tecnologías'
            ],
            'beneficios': [
                'Mejora de competencias del personal',
                'Reducción de accidentes laborales',
                'Incremento de productividad',
                'Desarrollo profesional continuo',
                'Cumplimiento de estándares de seguridad',
                'Retención de talento'
            ],
            'icono': 'fas fa-graduation-cap',
            'orden': 8
        }
    ]
    
    for servicio_data in servicios_data:
        Servicio.objects.create(**servicio_data)
    
    # 4. Categorías de Proyectos
    print("🏗️ Creando categorías de proyectos...")
    categorias_proyectos_data = [
        {
            'nombre': 'Minería Subterránea',
            'descripcion': 'Proyectos de extracción de minerales mediante técnicas de minería subterránea',
            'icono': 'fas fa-mountain',
            'orden': 1
        },
        {
            'nombre': 'Procesamiento',
            'descripcion': 'Plantas de procesamiento y beneficio de minerales',
            'icono': 'fas fa-industry',
            'orden': 2
        },
        {
            'nombre': 'Infraestructura',
            'descripcion': 'Desarrollo de infraestructura minera y de soporte',
            'icono': 'fas fa-road',
            'orden': 3
        },
        {
            'nombre': 'Exploración',
            'descripcion': 'Proyectos de exploración geológica y evaluación de recursos',
            'icono': 'fas fa-search',
            'orden': 4
        },
        {
            'nombre': 'Gestión Ambiental',
            'descripcion': 'Proyectos de manejo ambiental y rehabilitación',
            'icono': 'fas fa-leaf',
            'orden': 5
        },
        {
            'nombre': 'Logística',
            'descripcion': 'Proyectos de transporte y exportación de minerales',
            'icono': 'fas fa-ship',
            'orden': 6
        },
        {
            'nombre': 'Innovación Tecnológica',
            'descripcion': 'Proyectos de innovación y desarrollo tecnológico',
            'icono': 'fas fa-lightbulb',
            'orden': 7
        }
    ]
    
    for cat_data in categorias_proyectos_data:
        CategoriaProyecto.objects.create(**cat_data)
    
    # 5. Proyectos
    print("📊 Creando proyectos...")
    proyectos_data = [
        {
            'nombre': 'Proyecto Rampa Nueva Jerusalén',
            'slug': 'proyecto-rampa-nueva-jerusalen',
            'descripcion_corta': 'Proyecto principal de minería subterránea para la extracción de oro en el distrito de Sancos, Lucanas, Ayacucho.',
            'descripcion_larga': '''
            <h3>Descripción del Proyecto</h3>
            <p>El Proyecto Rampa Nueva Jerusalén representa la principal operación de Minera Fidami S.A., ubicado en el distrito de Sancos, provincia de Lucanas, departamento de Ayacucho. Este proyecto de minería subterránea está diseñado para la extracción eficiente y sostenible de mineral aurífero.</p>
            
            <h3>Infraestructura Principal</h3>
            <ul>
                <li><strong>Rampa Principal:</strong> Acceso subterráneo de 6x6 metros con pendiente del 15%</li>
                <li><strong>Galerías de Desarrollo:</strong> Red de túneles de 4x4 metros para acceso a zonas de explotación</li>
                <li><strong>Cámaras de Explotación:</strong> Método de cámaras y pilares con dimensiones optimizadas</li>
                <li><strong>Sistema de Ventilación:</strong> Ventilación forzada con capacidad de 500 m³/min</li>
                <li><strong>Planta de Procesamiento:</strong> Capacidad de 500 TPD para tratamiento de mineral</li>
            </ul>
            
            <h3>Características Técnicas</h3>
            <ul>
                <li><strong>Profundidad:</strong> Hasta 300 metros bajo superficie</li>
                <li><strong>Ley Promedio:</strong> 8.5 g/t Au</li>
                <li><strong>Vida Útil:</strong> 15 años</li>
                <li><strong>Producción Anual:</strong> 150,000 toneladas de mineral</li>
                <li><strong>Recuperación:</strong> 95% de oro</li>
            </ul>
            
            <h3>Beneficios del Proyecto</h3>
            <ul>
                <li>Generación de empleo directo e indirecto</li>
                <li>Desarrollo económico de la región</li>
                <li>Transferencia de tecnología minera</li>
                <li>Cumplimiento de estándares ambientales</li>
                <li>Contribución al desarrollo sostenible</li>
            </ul>
            ''',
            'categoria': CategoriaProyecto.objects.get(nombre='Minería Subterránea'),
            'estado_proyecto': 'en_curso',
            'fecha_inicio': date(2022, 3, 15),
            'fecha_fin_estimada': date(2037, 12, 31),
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'presupuesto': 25000000,
            'moneda': 'USD',
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800',
            'orden': 1
        },
        {
            'nombre': 'Planta de Procesamiento de Minerales',
            'slug': 'planta-procesamiento-minerales',
            'descripcion_corta': 'Planta moderna de procesamiento de minerales con capacidad de 500 TPD para el tratamiento de mineral aurífero.',
            'descripcion_larga': '''
            <h3>Descripción de la Planta</h3>
            <p>La Planta de Procesamiento de Minerales de Minera Fidami S.A. es una instalación moderna diseñada para el tratamiento eficiente de mineral aurífero proveniente del proyecto Rampa Nueva Jerusalén. La planta opera con tecnología de punta y está optimizada para maximizar la recuperación de oro.</p>
            
            <h3>Proceso de Procesamiento</h3>
            <ol>
                <li><strong>Recepción y Almacenamiento:</strong> Mineral recibido y almacenado en stockpile</li>
                <li><strong>Chancado Primario:</strong> Reducción de tamaño a 6" con chancadora de mandíbulas</li>
                <li><strong>Chancado Secundario:</strong> Reducción a 1" con chancadora cónica</li>
                <li><strong>Molienda:</strong> Molienda en molino de bolas hasta 80% -200 mallas</li>
                <li><strong>Flotación:</strong> Concentración por flotación de sulfuros</li>
                <li><strong>Cianuración:</strong> Lixiviación con cianuro de sodio</li>
                <li><strong>Recuperación:</strong> Adsorción en carbón activado</li>
                <li><strong>Refinación:</strong> Obtención de doré de oro</li>
            </ol>
            
            <h3>Especificaciones Técnicas</h3>
            <ul>
                <li><strong>Capacidad:</strong> 500 toneladas por día</li>
                <li><strong>Recuperación:</strong> 95% de oro</li>
                <li><strong>Consumo de Energía:</strong> Optimizado con motores de alta eficiencia</li>
                <li><strong>Control de Calidad:</strong> Laboratorio integrado con análisis en línea</li>
                <li><strong>Automatización:</strong> Sistema SCADA para control de procesos</li>
            </ul>
            
            <h3>Gestión Ambiental</h3>
            <ul>
                <li>Sistema de tratamiento de aguas residuales</li>
                <li>Recuperación y reutilización de agua de proceso</li>
                <li>Control de emisiones atmosféricas</li>
                <li>Manejo seguro de reactivos químicos</li>
                <li>Monitoreo ambiental continuo</li>
            </ul>
            ''',
            'categoria': CategoriaProyecto.objects.get(nombre='Procesamiento'),
            'estado_proyecto': 'completado',
            'fecha_inicio': date(2021, 8, 1),
            'fecha_fin_estimada': date(2022, 2, 28),
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'presupuesto': 8000000,
            'moneda': 'USD',
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800',
            'orden': 2
        },
        {
            'nombre': 'Sistema de Ventilación Subterránea',
            'slug': 'sistema-ventilacion-subterranea',
            'descripcion_corta': 'Sistema integral de ventilación subterránea para garantizar la seguridad y eficiencia operacional.',
            'descripcion_larga': '''
            <h3>Sistema de Ventilación</h3>
            <p>El Sistema de Ventilación Subterránea de Minera Fidami S.A. está diseñado para garantizar condiciones de trabajo seguras y saludables en todas las operaciones subterráneas. El sistema incluye ventilación principal, secundaria y de emergencia.</p>
            
            <h3>Componentes del Sistema</h3>
            <ul>
                <li><strong>Ventilador Principal:</strong> Ventilador axial de 500 HP con capacidad de 500 m³/min</li>
                <li><strong>Ductos de Ventilación:</strong> Ductos de fibra de vidrio de 1.2 metros de diámetro</li>
                <li><strong>Reguladores de Aire:</strong> Compuertas automáticas para control de flujo</li>
                <li><strong>Monitoreo de Gases:</strong> Sensores de CO, NOx, SO2 y partículas</li>
                <li><strong>Sistema de Emergencia:</strong> Ventilación de respaldo con generador diesel</li>
            </ul>
            
            <h3>Características Técnicas</h3>
            <ul>
                <li><strong>Capacidad Total:</strong> 500 m³/min de aire fresco</li>
                <li><strong>Presión Estática:</strong> 2,500 Pa</li>
                <li><strong>Eficiencia Energética:</strong> Motores IE3 de alta eficiencia</li>
                <li><strong>Control Automático:</strong> Sistema SCADA para monitoreo y control</li>
                <li><strong>Mantenimiento:</strong> Programa preventivo y predictivo</li>
            </ul>
            
            <h3>Beneficios del Sistema</h3>
            <ul>
                <li>Condiciones de trabajo seguras</li>
                <li>Cumplimiento de estándares de seguridad</li>
                <li>Reducción de riesgos para la salud</li>
                <li>Optimización energética</li>
                <li>Monitoreo continuo de calidad del aire</li>
            </ul>
            ''',
            'categoria': CategoriaProyecto.objects.get(nombre='Infraestructura'),
            'estado_proyecto': 'en_curso',
            'fecha_inicio': date(2022, 1, 15),
            'fecha_fin_estimada': date(2022, 6, 30),
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'presupuesto': 3500000,
            'moneda': 'USD',
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800',
            'orden': 3
        },
        {
            'nombre': 'Exploración Cerro San Pedro',
            'slug': 'exploracion-cerro-san-pedro',
            'descripcion_corta': 'Proyecto de exploración geológica en el Cerro San Pedro, distrito de Sancos.',
            'descripcion_larga': 'Proyecto de exploración geológica en el Cerro San Pedro, ubicado en el distrito de Sancos, provincia de Lucanas, Ayacucho. Incluye mapeo geológico, perforación diamantina y análisis geoquímicos.',
            'categoria': CategoriaProyecto.objects.get(nombre='Exploración'),
            'estado_proyecto': 'en_curso',
            'fecha_inicio': date(2023, 6, 1),
            'fecha_fin_estimada': date(2024, 12, 31),
            'ubicacion': 'Cerro San Pedro, Sancos, Lucanas, Ayacucho',
            'presupuesto': 5000000,
            'moneda': 'USD',
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800',
            'orden': 4
        },
        {
            'nombre': 'Desarrollo Comunitario Sancos',
            'slug': 'desarrollo-comunitario-sancos',
            'descripcion_corta': 'Programa integral de desarrollo comunitario para el distrito de Sancos.',
            'descripcion_larga': 'Programa integral de desarrollo comunitario en el distrito de Sancos, incluyendo educación, salud, infraestructura y desarrollo económico local.',
            'categoria': CategoriaProyecto.objects.get(nombre='Gestión Ambiental'),
            'estado_proyecto': 'en_curso',
            'fecha_inicio': date(2021, 1, 1),
            'fecha_fin_estimada': date(2025, 12, 31),
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'presupuesto': 3000000,
            'moneda': 'USD',
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800',
            'orden': 5
        },
        {
            'nombre': 'Optimización de Procesos Mineros',
            'slug': 'optimizacion-procesos-mineros',
            'descripcion_corta': 'Proyecto de optimización de procesos mineros para mejorar la eficiencia operacional.',
            'descripcion_larga': 'Proyecto de optimización de procesos mineros en el proyecto Rampa Nueva Jerusalén, implementando nuevas tecnologías y mejores prácticas.',
            'categoria': CategoriaProyecto.objects.get(nombre='Innovación Tecnológica'),
            'estado_proyecto': 'en_curso',
            'fecha_inicio': date(2023, 1, 1),
            'fecha_fin_estimada': date(2024, 6, 30),
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'presupuesto': 2000000,
            'moneda': 'USD',
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800',
            'orden': 6
        }
    ]
    
    for proyecto_data in proyectos_data:
        Proyecto.objects.create(**proyecto_data)
    
    # 6. Tecnologías
    print("💡 Creando tecnologías...")
    tecnologias_data = [
        {
            'nombre': 'Sistema de Ventilación Inteligente',
            'slug': 'sistema-ventilacion-inteligente',
            'descripcion_corta': 'Sistema de ventilación subterránea con control automático y monitoreo en tiempo real de gases y calidad del aire.',
            'descripcion_larga': 'Sistema avanzado de ventilación subterránea que utiliza sensores inteligentes y control automático para optimizar la calidad del aire en operaciones mineras subterráneas.',
            'categoria': 'seguridad',
            'beneficios': ['Seguridad mejorada', 'Eficiencia energética', 'Monitoreo continuo'],
            'aplicaciones': ['Minería subterránea', 'Túneles', 'Espacios confinados'],
            'estado': 'activo',
            'orden': 1
        },
        {
            'nombre': 'Perforación Automatizada',
            'slug': 'perforacion-automatizada',
            'descripcion_corta': 'Equipos de perforación con control automático y GPS subterráneo para mayor precisión y eficiencia.',
            'descripcion_larga': 'Tecnología de perforación automatizada que integra GPS subterráneo y control automático para maximizar la precisión y eficiencia en el desarrollo de túneles y rampas.',
            'categoria': 'eficiencia',
            'beneficios': ['Mayor precisión', 'Reducción de costos', 'Seguridad mejorada'],
            'aplicaciones': ['Desarrollo de túneles', 'Exploración geológica', 'Desarrollo de minas'],
            'estado': 'activo',
            'orden': 2
        },
        {
            'nombre': 'Procesamiento de Oro por Carbón Activado',
            'slug': 'procesamiento-oro-carbono-activado',
            'descripcion_corta': 'Tecnología avanzada de recuperación de oro mediante adsorción en carbón activado con alta eficiencia.',
            'descripcion_larga': 'Sistema de procesamiento de oro que utiliza carbón activado para la adsorción y recuperación eficiente de oro de soluciones cianuradas.',
            'categoria': 'mineria',
            'beneficios': ['Recuperación del 95%', 'Bajo consumo de reactivos', 'Proceso automatizado'],
            'aplicaciones': ['Planta de procesamiento', 'Recuperación de oro', 'Procesamiento de minerales'],
            'estado': 'activo',
            'orden': 3
        },
        {
            'nombre': 'Monitoreo Geotécnico en Tiempo Real',
            'slug': 'monitoreo-geotecnico-tiempo-real',
            'descripcion_corta': 'Sistema de sensores y monitoreo continuo de la estabilidad de taludes y estructuras subterráneas.',
            'descripcion_larga': 'Sistema integral de monitoreo geotécnico que utiliza sensores avanzados para el seguimiento continuo de la estabilidad de taludes y estructuras subterráneas.',
            'categoria': 'seguridad',
            'beneficios': ['Prevención de accidentes', 'Datos en tiempo real', 'Alertas automáticas'],
            'aplicaciones': ['Monitoreo de taludes', 'Estabilidad de estructuras', 'Prevención de riesgos'],
            'estado': 'activo',
            'orden': 4
        },
        {
            'nombre': 'Flotación Selectiva de Minerales',
            'slug': 'flotacion-selectiva-minerales',
            'descripcion_corta': 'Tecnología de flotación selectiva para separación eficiente de minerales auríferos.',
            'descripcion_larga': 'Proceso de flotación selectiva que permite la separación eficiente de minerales auríferos mediante el uso de reactivos específicos y control de parámetros.',
            'categoria': 'mineria',
            'beneficios': ['Mayor recuperación', 'Menor consumo de reactivos', 'Proceso optimizado'],
            'aplicaciones': ['Procesamiento de minerales', 'Separación de minerales', 'Concentración de oro'],
            'estado': 'activo',
            'orden': 5
        },
        {
            'nombre': 'Sistema de Drenaje Subterráneo',
            'slug': 'sistema-drenaje-subterraneo',
            'descripcion_corta': 'Sistema integral de drenaje para control de aguas subterráneas en operaciones mineras.',
            'descripcion_larga': 'Sistema avanzado de drenaje subterráneo que controla eficientemente las aguas subterráneas en operaciones mineras, garantizando la estabilidad operacional.',
            'categoria': 'ambiental',
            'beneficios': ['Control de aguas', 'Estabilidad operacional', 'Cumplimiento ambiental'],
            'aplicaciones': ['Control de aguas subterráneas', 'Estabilidad de minas', 'Gestión ambiental'],
            'estado': 'activo',
            'orden': 6
        },
        {
            'nombre': 'Automatización de Plantas de Procesamiento',
            'slug': 'automatizacion-plantas-procesamiento',
            'descripcion_corta': 'Sistema SCADA para control y automatización completa de plantas de procesamiento de minerales.',
            'descripcion_larga': 'Sistema SCADA integral que permite el control y automatización completa de plantas de procesamiento de minerales, optimizando todos los procesos.',
            'categoria': 'digital',
            'beneficios': ['Operación 24/7', 'Optimización de procesos', 'Reducción de errores'],
            'aplicaciones': ['Control de procesos', 'Automatización industrial', 'Optimización de plantas'],
            'estado': 'activo',
            'orden': 7
        },
        {
            'nombre': 'Tecnología de Lixiviación en Pilas',
            'slug': 'tecnologia-lixiviacion-pilas',
            'descripcion_corta': 'Sistema de lixiviación en pilas para tratamiento de minerales de baja ley.',
            'descripcion_larga': 'Tecnología de lixiviación en pilas que permite el tratamiento eficiente de minerales de baja ley mediante procesos de lixiviación controlada.',
            'categoria': 'mineria',
            'beneficios': ['Tratamiento de baja ley', 'Bajo costo operativo', 'Proceso ambientalmente amigable'],
            'aplicaciones': ['Tratamiento de minerales', 'Lixiviación de oro', 'Procesamiento de baja ley'],
            'estado': 'activo',
            'orden': 8
        }
    ]
    
    for tecnologia_data in tecnologias_data:
        Tecnologia.objects.create(**tecnologia_data)
    
    # 7. Proyectos de Innovación
    print("🚀 Creando proyectos de innovación...")
    proyectos_innovacion_data = [
        {
            'nombre': 'Sistema de Ventilación Inteligente',
            'slug': 'sistema-ventilacion-inteligente',
            'descripcion_corta': 'Desarrollo de sistema de ventilación subterránea con control automático y monitoreo en tiempo real.',
            'descripcion_larga': 'Proyecto de desarrollo de un sistema avanzado de ventilación subterránea que integra control automático y monitoreo en tiempo real de gases y calidad del aire.',
            'tipo_proyecto': 'desarrollo',
            'estado_proyecto': 'desarrollo',
            'tecnologias_utilizadas': ['Sensores IoT', 'Control automático', 'Monitoreo en tiempo real'],
            'equipo_investigacion': ['Juan Carlos Rodríguez', 'Carlos Mendoza'],
            'presupuesto': 1500000,
            'moneda': 'USD',
            'fecha_inicio': date(2023, 1, 15),
            'fecha_fin_estimada': date(2024, 6, 30),
            'resultados': ['Reducción del 30% en consumo energético', 'Mejora en calidad del aire'],
            'impacto_esperado': 'Mejora significativa en la seguridad y eficiencia energética de las operaciones subterráneas',
            'estado': 'activo',
            'orden': 1
        },
        {
            'nombre': 'Automatización de Perforación',
            'slug': 'automatizacion-perforacion',
            'descripcion_corta': 'Implementación de sistemas automatizados para perforación subterránea con GPS integrado.',
            'descripcion_larga': 'Proyecto de implementación de sistemas automatizados para perforación subterránea que integra GPS y control automático para mayor precisión.',
            'tipo_proyecto': 'implementacion',
            'estado_proyecto': 'finalizado',
            'tecnologias_utilizadas': ['GPS subterráneo', 'Control automático', 'Perforadoras inteligentes'],
            'equipo_investigacion': ['Juan Carlos Rodríguez', 'Carlos Mendoza'],
            'presupuesto': 2000000,
            'moneda': 'USD',
            'fecha_inicio': date(2022, 8, 1),
            'fecha_fin_estimada': date(2023, 12, 31),
            'fecha_fin_real': date(2023, 12, 31),
            'resultados': ['Incremento del 25% en precisión', 'Reducción del 20% en costos'],
            'impacto_esperado': 'Mejora significativa en la precisión y eficiencia de las operaciones de perforación',
            'estado': 'activo',
            'orden': 2
        },
        {
            'nombre': 'Optimización de Procesamiento de Oro',
            'slug': 'optimizacion-procesamiento-oro',
            'descripcion_corta': 'Mejora de procesos de recuperación de oro mediante nuevas tecnologías de flotación y cianuración.',
            'descripcion_larga': 'Proyecto de optimización de procesos de recuperación de oro que implementa nuevas tecnologías de flotación selectiva y cianuración optimizada.',
            'tipo_proyecto': 'desarrollo',
            'estado_proyecto': 'desarrollo',
            'tecnologias_utilizadas': ['Flotación selectiva', 'Cianuración optimizada', 'Control de procesos'],
            'equipo_investigacion': ['Ana Torres', 'María Elena López'],
            'presupuesto': 1800000,
            'moneda': 'USD',
            'fecha_inicio': date(2023, 3, 1),
            'fecha_fin_estimada': date(2024, 9, 30),
            'resultados': ['Recuperación del 95%', 'Reducción del 15% en reactivos'],
            'impacto_esperado': 'Incremento significativo en la recuperación de oro y reducción de costos operativos',
            'estado': 'activo',
            'orden': 3
        },
        {
            'nombre': 'Sistema de Monitoreo Geotécnico',
            'slug': 'sistema-monitoreo-geotecnico',
            'descripcion_corta': 'Desarrollo de sistema de sensores para monitoreo continuo de estabilidad de taludes y estructuras.',
            'descripcion_larga': 'Proyecto de desarrollo de un sistema integral de sensores para el monitoreo continuo de la estabilidad de taludes y estructuras subterráneas.',
            'tipo_proyecto': 'desarrollo',
            'estado_proyecto': 'finalizado',
            'tecnologias_utilizadas': ['Sensores de deformación', 'Monitoreo en tiempo real', 'Alertas automáticas'],
            'equipo_investigacion': ['Roberto Vargas', 'Carlos Mendoza'],
            'presupuesto': 1200000,
            'moneda': 'USD',
            'fecha_inicio': date(2022, 5, 1),
            'fecha_fin_estimada': date(2023, 2, 28),
            'fecha_fin_real': date(2023, 2, 28),
            'resultados': ['Sistema operativo', 'Reducción de riesgos geotécnicos'],
            'impacto_esperado': 'Prevención efectiva de accidentes geotécnicos y mejora en la seguridad operacional',
            'estado': 'activo',
            'orden': 4
        },
        {
            'nombre': 'Gestión Inteligente de Residuos',
            'slug': 'gestion-inteligente-residuos',
            'descripcion_corta': 'Implementación de tecnologías avanzadas para el manejo y tratamiento de relaves mineros.',
            'descripcion_larga': 'Proyecto de implementación de tecnologías avanzadas para el manejo y tratamiento integral de relaves mineros con enfoque en sostenibilidad.',
            'tipo_proyecto': 'implementacion',
            'estado_proyecto': 'desarrollo',
            'tecnologias_utilizadas': ['Tratamiento de relaves', 'Recuperación de agua', 'Estabilización'],
            'equipo_investigacion': ['Ana Torres', 'Lucía Quispe'],
            'presupuesto': 2500000,
            'moneda': 'USD',
            'fecha_inicio': date(2023, 6, 1),
            'fecha_fin_estimada': date(2024, 12, 31),
            'resultados': ['Reutilización del 80% del agua', 'Cumplimiento ambiental total'],
            'impacto_esperado': 'Reducción significativa del impacto ambiental y optimización del uso de recursos hídricos',
            'estado': 'activo',
            'orden': 5
        },
        {
            'nombre': 'Plataforma de Gestión de Datos Mineros',
            'slug': 'plataforma-gestion-datos-mineros',
            'descripcion_corta': 'Desarrollo de plataforma digital para gestión integral de datos operacionales y análisis predictivo.',
            'descripcion_larga': 'Proyecto de desarrollo de una plataforma digital integral para la gestión de datos operacionales y análisis predictivo en minería.',
            'tipo_proyecto': 'desarrollo',
            'estado_proyecto': 'desarrollo',
            'tecnologias_utilizadas': ['Big Data', 'Inteligencia Artificial', 'Análisis predictivo'],
            'equipo_investigacion': ['Juan Carlos Rodríguez', 'María Elena López'],
            'presupuesto': 1000000,
            'moneda': 'USD',
            'fecha_inicio': date(2023, 9, 1),
            'fecha_fin_estimada': date(2024, 8, 31),
            'resultados': ['Plataforma operativa', 'Mejora en toma de decisiones'],
            'impacto_esperado': 'Optimización de procesos operacionales mediante análisis de datos y toma de decisiones informada',
            'estado': 'activo',
            'orden': 6
        },
        {
            'nombre': 'Sistema de Energía Renovable',
            'slug': 'sistema-energia-renovable',
            'descripcion_corta': 'Implementación de sistemas de energía solar y eólica para reducir la huella de carbono.',
            'descripcion_larga': 'Proyecto de implementación de sistemas de energía solar y eólica para reducir la huella de carbono de las operaciones mineras.',
            'tipo_proyecto': 'implementacion',
            'estado_proyecto': 'planificacion',
            'tecnologias_utilizadas': ['Energía solar', 'Energía eólica', 'Almacenamiento de energía'],
            'equipo_investigacion': ['María Elena López', 'Ana Torres'],
            'presupuesto': 3000000,
            'moneda': 'USD',
            'fecha_inicio': date(2024, 1, 1),
            'fecha_fin_estimada': date(2025, 6, 30),
            'resultados': ['Reducción del 40% en emisiones', 'Ahorro energético del 25%'],
            'impacto_esperado': 'Reducción significativa de la huella de carbono y costos energéticos',
            'estado': 'activo',
            'orden': 7
        },
        {
            'nombre': 'Tecnología de Recuperación de Agua',
            'slug': 'tecnologia-recuperacion-agua',
            'descripcion_corta': 'Desarrollo de sistemas avanzados para recuperación y reutilización de agua en procesos mineros.',
            'descripcion_larga': 'Proyecto de desarrollo de sistemas avanzados para la recuperación y reutilización eficiente de agua en procesos mineros.',
            'tipo_proyecto': 'desarrollo',
            'estado_proyecto': 'desarrollo',
            'tecnologias_utilizadas': ['Filtración avanzada', 'Tratamiento de aguas', 'Reutilización'],
            'equipo_investigacion': ['María Elena López', 'Ana Torres'],
            'presupuesto': 1600000,
            'moneda': 'USD',
            'fecha_inicio': date(2023, 7, 1),
            'fecha_fin_estimada': date(2024, 11, 30),
            'resultados': ['Recuperación del 90% del agua', 'Reducción del 60% en consumo'],
            'impacto_esperado': 'Optimización significativa del uso de recursos hídricos y reducción de costos operativos',
            'estado': 'activo',
            'orden': 8
        }
    ]
    
    for proyecto_data in proyectos_innovacion_data:
        ProyectoInnovacion.objects.create(**proyecto_data)
    
    # 8. Patentes
    print("📜 Creando patentes...")
    patentes_data = [
        {
            'titulo': 'Sistema de Ventilación Subterránea Inteligente',
            'slug': 'sistema-ventilacion-subterranea-inteligente',
            'descripcion': 'Sistema de ventilación subterránea con control automático y monitoreo en tiempo real de gases y calidad del aire.',
            'numero_patente': 'PE-2023-001234',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 3, 15),
            'fecha_aprobacion': date(2023, 8, 20),
            'fecha_expiracion': date(2043, 8, 20),
            'inventores': ['Juan Carlos Rodríguez', 'Carlos Mendoza'],
            'aplicacion_industrial': 'Minería subterránea, túneles, espacios confinados',
            'ventajas_tecnicas': ['Adaptación automática', 'Ahorro energético', 'Mayor seguridad'],
            'destacado': True,
            'orden': 1
        },
        {
            'titulo': 'Método de Recuperación de Oro Mejorado',
            'slug': 'metodo-recuperacion-oro-mejorado',
            'descripcion': 'Proceso mejorado de recuperación de oro mediante flotación selectiva y cianuración optimizada.',
            'numero_patente': 'PE-2023-001235',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 4, 10),
            'fecha_aprobacion': date(2023, 9, 15),
            'fecha_expiracion': date(2043, 9, 15),
            'inventores': ['Ana Torres', 'María Elena López'],
            'aplicacion_industrial': 'Procesamiento de minerales auríferos, plantas de concentración',
            'ventajas_tecnicas': ['Mayor recuperación', 'Menor consumo de reactivos', 'Proceso optimizado'],
            'destacado': True,
            'orden': 2
        },
        {
            'titulo': 'Sistema de Monitoreo Geotécnico en Tiempo Real',
            'slug': 'sistema-monitoreo-geotecnico-tiempo-real',
            'descripcion': 'Sistema de sensores y monitoreo continuo de la estabilidad de taludes y estructuras subterráneas.',
            'numero_patente': 'PE-2023-001236',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 5, 20),
            'fecha_aprobacion': date(2023, 10, 30),
            'fecha_expiracion': date(2043, 10, 30),
            'inventores': ['Roberto Vargas', 'Carlos Mendoza'],
            'aplicacion_industrial': 'Minería subterránea, ingeniería geotécnica, monitoreo de estructuras',
            'ventajas_tecnicas': ['Monitoreo continuo', 'Alertas automáticas', 'Prevención de accidentes'],
            'destacado': False,
            'orden': 3
        },
        {
            'titulo': 'Proceso de Tratamiento de Relaves Mejorado',
            'slug': 'proceso-tratamiento-relaves-mejorado',
            'descripcion': 'Método innovador para el tratamiento y estabilización de relaves mineros con reducción de impacto ambiental.',
            'numero_patente': 'PE-2023-001237',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 6, 5),
            'fecha_aprobacion': date(2023, 11, 12),
            'fecha_expiracion': date(2043, 11, 12),
            'inventores': ['Ana Torres', 'Lucía Quispe'],
            'aplicacion_industrial': 'Gestión de residuos mineros, tratamiento de relaves, protección ambiental',
            'ventajas_tecnicas': ['Reducción de impacto ambiental', 'Estabilización mejorada', 'Recuperación de agua'],
            'destacado': False,
            'orden': 4
        },
        {
            'titulo': 'Sistema de Perforación Automatizada con GPS',
            'slug': 'sistema-perforacion-automatizada-gps',
            'descripcion': 'Sistema de perforación subterránea con control automático y posicionamiento GPS integrado.',
            'numero_patente': 'PE-2023-001238',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 7, 15),
            'fecha_aprobacion': date(2023, 12, 20),
            'fecha_expiracion': date(2043, 12, 20),
            'inventores': ['Juan Carlos Rodríguez', 'Carlos Mendoza'],
            'aplicacion_industrial': 'Perforación subterránea, desarrollo de túneles, exploración minera',
            'ventajas_tecnicas': ['Mayor precisión', 'Control automático', 'Reducción de errores'],
            'destacado': False,
            'orden': 5
        },
        {
            'titulo': 'Método de Lixiviación en Pilas Optimizado',
            'slug': 'metodo-lixiviacion-pilas-optimizado',
            'descripcion': 'Proceso optimizado de lixiviación en pilas para tratamiento de minerales de baja ley.',
            'numero_patente': 'PE-2023-001239',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 8, 10),
            'fecha_aprobacion': date(2024, 1, 25),
            'fecha_expiracion': date(2044, 1, 25),
            'inventores': ['Ana Torres', 'María Elena López'],
            'aplicacion_industrial': 'Lixiviación de minerales, procesamiento de baja ley, recuperación de metales',
            'ventajas_tecnicas': ['Mayor recuperación', 'Menor consumo de reactivos', 'Proceso optimizado'],
            'destacado': False,
            'orden': 6
        },
        {
            'titulo': 'Sistema de Recuperación de Agua de Proceso',
            'slug': 'sistema-recuperacion-agua-proceso',
            'descripcion': 'Sistema integral para recuperación y reutilización de agua en procesos mineros.',
            'numero_patente': 'PE-2023-001240',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 9, 5),
            'fecha_aprobacion': date(2024, 2, 15),
            'fecha_expiracion': date(2044, 2, 15),
            'inventores': ['María Elena López', 'Ana Torres'],
            'aplicacion_industrial': 'Gestión de agua en minería, reutilización de recursos hídricos',
            'ventajas_tecnicas': ['Recuperación eficiente', 'Reutilización de agua', 'Reducción de consumo'],
            'destacado': False,
            'orden': 7
        },
        {
            'titulo': 'Plataforma de Gestión de Datos Mineros',
            'slug': 'plataforma-gestion-datos-mineros',
            'descripcion': 'Plataforma digital para gestión integral de datos operacionales y análisis predictivo en minería.',
            'numero_patente': 'PE-2023-001241',
            'tipo': 'patente',
            'estado': 'aprobada',
            'fecha_solicitud': date(2023, 10, 20),
            'fecha_aprobacion': date(2024, 3, 10),
            'fecha_expiracion': date(2044, 3, 10),
            'inventores': ['Juan Carlos Rodríguez', 'María Elena López'],
            'aplicacion_industrial': 'Gestión de datos mineros, análisis predictivo, optimización de procesos',
            'ventajas_tecnicas': ['Análisis predictivo', 'Optimización de decisiones', 'Gestión integral'],
            'destacado': False,
            'orden': 8
        }
    ]
    
    for patente_data in patentes_data:
        Patente.objects.create(**patente_data)
    
    # 9. Programas Sociales
    print("🤝 Creando programas sociales...")
    programas_sociales_data = [
        {
            'nombre': 'Programa de Educación Integral',
            'slug': 'programa-educacion-integral',
            'descripcion_corta': 'Programa integral de apoyo educativo para estudiantes de Sancos.',
            'descripcion_larga': 'Programa integral de apoyo educativo para estudiantes de Sancos, incluyendo mejoras de infraestructura y capacitación docente.',
            'categoria': 'educacion',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 1, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 500000,
            'moneda': 'USD',
            'beneficiarios_directos': 150,
            'beneficiarios_indirectos': 600,
            'objetivos': ['Mejorar la calidad educativa', 'Reducir la deserción escolar', 'Capacitar docentes'],
            'resultados': ['Incremento del 40% en rendimiento académico', '3 escuelas mejoradas'],
            'impacto_social': 'Incremento del 40% en rendimiento académico',
            'estado': 'activo',
            'orden': 1
        },
        {
            'nombre': 'Programa de Salud Comunitaria',
            'slug': 'programa-salud-comunitaria',
            'descripcion_corta': 'Programa de atención médica preventiva y curativa para la comunidad de Sancos.',
            'descripcion_larga': 'Programa de atención médica preventiva y curativa para la comunidad de Sancos, incluyendo capacitación de promotores de salud.',
            'categoria': 'salud',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 3, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 300000,
            'moneda': 'USD',
            'beneficiarios_directos': 500,
            'beneficiarios_indirectos': 2000,
            'objetivos': ['Mejorar la salud preventiva', 'Reducir enfermedades', 'Capacitar promotores de salud'],
            'resultados': ['Reducción del 30% en enfermedades respiratorias', '1 centro de salud equipado'],
            'impacto_social': 'Reducción del 30% en enfermedades respiratorias',
            'estado': 'activo',
            'orden': 2
        },
        {
            'nombre': 'Programa de Desarrollo Económico Local',
            'slug': 'programa-desarrollo-economico-local',
            'descripcion_corta': 'Apoyo a emprendimientos locales y desarrollo de capacidades productivas en Sancos.',
            'descripcion_larga': 'Programa de apoyo a emprendimientos locales y desarrollo de capacidades productivas en Sancos para mejorar los ingresos familiares.',
            'categoria': 'empleo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 6, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 200000,
            'moneda': 'USD',
            'beneficiarios_directos': 50,
            'beneficiarios_indirectos': 200,
            'objetivos': ['Crear empleo local', 'Fortalecer emprendimientos', 'Mejorar ingresos familiares'],
            'resultados': ['Creación de 25 nuevos empleos locales', '10 emprendimientos apoyados'],
            'impacto_social': 'Creación de 25 nuevos empleos locales',
            'estado': 'activo',
            'orden': 3
        },
        {
            'nombre': 'Programa de Infraestructura Rural',
            'slug': 'programa-infraestructura-rural',
            'descripcion_corta': 'Mejora de infraestructura rural incluyendo caminos, sistemas de agua y electrificación.',
            'descripcion_larga': 'Programa de mejora de infraestructura rural incluyendo caminos, sistemas de agua potable y electrificación en Sancos.',
            'categoria': 'infraestructura',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 8, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 800000,
            'moneda': 'USD',
            'beneficiarios_directos': 300,
            'beneficiarios_indirectos': 1200,
            'objetivos': ['Mejorar conectividad', 'Proveer agua potable', 'Electrificación rural'],
            'resultados': ['15 km de caminos mejorados', '2 sistemas de agua potable'],
            'impacto_social': '15 km de caminos mejorados, 2 sistemas de agua',
            'estado': 'activo',
            'orden': 4
        },
        {
            'nombre': 'Programa de Capacitación Técnica',
            'slug': 'programa-capacitacion-tecnica',
            'descripcion_corta': 'Capacitación técnica especializada para jóvenes y adultos de Sancos en diferentes oficios.',
            'descripcion_larga': 'Programa de capacitación técnica especializada para jóvenes y adultos de Sancos en diferentes oficios relacionados con la minería.',
            'categoria': 'empleo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 9, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 250000,
            'moneda': 'USD',
            'beneficiarios_directos': 100,
            'beneficiarios_indirectos': 400,
            'objetivos': ['Desarrollar habilidades técnicas', 'Mejorar empleabilidad', 'Transferir conocimientos'],
            'resultados': ['80% de capacitados empleados', '100 personas capacitadas'],
            'impacto_social': '80% de capacitados empleados en el sector minero',
            'estado': 'activo',
            'orden': 5
        },
        {
            'nombre': 'Programa de Conservación Ambiental',
            'slug': 'programa-conservacion-ambiental',
            'descripcion_corta': 'Programa de educación ambiental y conservación de recursos naturales en la región de Sancos.',
            'descripcion_larga': 'Programa de educación ambiental y conservación de recursos naturales en la región de Sancos, incluyendo proyectos de reforestación.',
            'categoria': 'medio_ambiente',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 10, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 150000,
            'moneda': 'USD',
            'beneficiarios_directos': 200,
            'beneficiarios_indirectos': 800,
            'objetivos': ['Educar en conservación', 'Proteger recursos naturales', 'Promover prácticas sostenibles'],
            'resultados': ['Implementación de 5 proyectos de conservación', '200 personas educadas'],
            'impacto_social': 'Implementación de 5 proyectos de conservación',
            'estado': 'activo',
            'orden': 6
        },
        {
            'nombre': 'Programa de Apoyo a la Agricultura',
            'slug': 'programa-apoyo-agricultura',
            'descripcion_corta': 'Apoyo técnico y financiero para mejorar la producción agrícola en Sancos.',
            'descripcion_larga': 'Programa de apoyo técnico y financiero para mejorar la producción agrícola en Sancos, incluyendo diversificación de cultivos.',
            'categoria': 'empleo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 11, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 100000,
            'moneda': 'USD',
            'beneficiarios_directos': 80,
            'beneficiarios_indirectos': 320,
            'objetivos': ['Mejorar producción agrícola', 'Diversificar cultivos', 'Mejorar técnicas de riego'],
            'resultados': ['Incremento del 50% en producción agrícola', '80 agricultores beneficiados'],
            'impacto_social': 'Incremento del 50% en producción agrícola',
            'estado': 'activo',
            'orden': 7
        },
        {
            'nombre': 'Programa de Fortalecimiento Institucional',
            'slug': 'programa-fortalecimiento-institucional',
            'descripcion_corta': 'Apoyo al fortalecimiento de organizaciones comunitarias y autoridades locales de Sancos.',
            'descripcion_larga': 'Programa de apoyo al fortalecimiento de organizaciones comunitarias y autoridades locales de Sancos para mejorar la gestión local.',
            'categoria': 'educacion',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2021, 12, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 80000,
            'moneda': 'USD',
            'beneficiarios_directos': 30,
            'beneficiarios_indirectos': 1500,
            'objetivos': ['Fortalecer organizaciones', 'Mejorar gestión local', 'Promover participación ciudadana'],
            'resultados': ['5 organizaciones comunitarias fortalecidas', '30 líderes capacitados'],
            'impacto_social': '5 organizaciones comunitarias fortalecidas',
            'estado': 'activo',
            'orden': 8
        }
    ]
    
    for programa_data in programas_sociales_data:
        ProgramaSocial.objects.create(**programa_data)
    
    # 10. Alianzas
    print("🤝 Creando alianzas...")
    alianzas_data = [
        {
            'nombre': 'Alianza con Universidad Nacional de San Cristóbal de Huamanga',
            'slug': 'alianza-unsch',
            'descripcion': 'Alianza estratégica con la Universidad Nacional de San Cristóbal de Huamanga para investigación y desarrollo en minería sostenible.',
            'tipo_alianza': 'universidad',
            'organizacion': 'Universidad Nacional de San Cristóbal de Huamanga',
            'contacto_principal': 'Dr. Carlos Mendoza',
            'email_contacto': 'carlos.mendoza@unsch.edu.pe',
            'telefono_contacto': '+51 966123456',
            'fecha_inicio': date(2023, 7, 1),
            'fecha_fin': date(2025, 6, 30),
            'objetivos': ['Investigación conjunta', 'Capacitación de estudiantes', 'Desarrollo de proyectos'],
            'resultados': ['5 proyectos de investigación', '50 estudiantes beneficiados'],
            'estado': 'activa',
            'orden': 1
        },
        {
            'nombre': 'Alianza con Gobierno Regional de Ayacucho',
            'slug': 'alianza-gobierno-ayacucho',
            'descripcion': 'Alianza con el Gobierno Regional de Ayacucho para el desarrollo sostenible de la región.',
            'tipo_alianza': 'gobierno',
            'organizacion': 'Gobierno Regional de Ayacucho',
            'contacto_principal': 'Ing. María López',
            'email_contacto': 'mlopez@gobiernoayacucho.gob.pe',
            'telefono_contacto': '+51 966789012',
            'fecha_inicio': date(2023, 8, 1),
            'fecha_fin': date(2025, 12, 31),
            'objetivos': ['Desarrollo regional', 'Infraestructura pública', 'Capacitación laboral'],
            'resultados': ['3 proyectos de infraestructura', '200 personas capacitadas'],
            'estado': 'activa',
            'orden': 2
        },
        {
            'nombre': 'Alianza con SENATI',
            'slug': 'alianza-senati',
            'descripcion': 'Alianza con SENATI para la capacitación técnica especializada en minería.',
            'tipo_alianza': 'universidad',
            'organizacion': 'SENATI',
            'contacto_principal': 'Lic. Roberto Vargas',
            'email_contacto': 'rvargas@senati.edu.pe',
            'telefono_contacto': '+51 966345678',
            'fecha_inicio': date(2023, 9, 1),
            'fecha_fin': date(2025, 8, 31),
            'objetivos': ['Capacitación técnica', 'Formación de operadores', 'Desarrollo de competencias'],
            'resultados': ['100 operadores capacitados', '5 programas técnicos'],
            'estado': 'activa',
            'orden': 3
        },
        {
            'nombre': 'Alianza con Comunidad Campesina de Sancos',
            'slug': 'alianza-comunidad-sancos',
            'descripcion': 'Alianza estratégica con la Comunidad Campesina de Sancos para el desarrollo comunitario.',
            'tipo_alianza': 'comunidad',
            'organizacion': 'Comunidad Campesina de Sancos',
            'contacto_principal': 'Sra. María Quispe',
            'email_contacto': 'mquispe@comunidadsancos.org',
            'telefono_contacto': '+51 966901234',
            'fecha_inicio': date(2023, 6, 1),
            'fecha_fin': date(2026, 5, 31),
            'objetivos': ['Desarrollo comunitario', 'Preservación cultural', 'Beneficio mutuo'],
            'resultados': ['8 programas comunitarios', '500 familias beneficiadas'],
            'estado': 'activa',
            'orden': 4
        },
        {
            'nombre': 'Alianza con Ministerio de Energía y Minas',
            'slug': 'alianza-minem',
            'descripcion': 'Alianza con el Ministerio de Energía y Minas para el cumplimiento de estándares mineros.',
            'tipo_alianza': 'gobierno',
            'organizacion': 'Ministerio de Energía y Minas',
            'contacto_principal': 'Ing. Juan Carlos Rodríguez',
            'email_contacto': 'jrodriguez@minem.gob.pe',
            'telefono_contacto': '+51 966567890',
            'fecha_inicio': date(2023, 5, 1),
            'fecha_fin': date(2025, 4, 30),
            'objetivos': ['Cumplimiento normativo', 'Mejores prácticas', 'Desarrollo sostenible'],
            'resultados': ['Cumplimiento total de estándares', '3 certificaciones obtenidas'],
            'estado': 'activa',
            'orden': 5
        },
        {
            'nombre': 'Alianza con Universidad Nacional de Ingeniería',
            'slug': 'alianza-uni',
            'descripcion': 'Alianza con la Universidad Nacional de Ingeniería para investigación en tecnología minera.',
            'tipo_alianza': 'universidad',
            'organizacion': 'Universidad Nacional de Ingeniería',
            'contacto_principal': 'Dr. Ana Torres',
            'email_contacto': 'atorres@uni.edu.pe',
            'telefono_contacto': '+51 966123789',
            'fecha_inicio': date(2023, 10, 1),
            'fecha_fin': date(2025, 9, 30),
            'objetivos': ['Investigación tecnológica', 'Desarrollo de innovaciones', 'Capacitación especializada'],
            'resultados': ['3 patentes desarrolladas', '20 investigadores involucrados'],
            'estado': 'activa',
            'orden': 6
        },
        {
            'nombre': 'Alianza con ONG Ambiental',
            'slug': 'alianza-ong-ambiental',
            'descripcion': 'Alianza con organización no gubernamental para proyectos de conservación ambiental.',
            'tipo_alianza': 'ong',
            'organizacion': 'ONG Conservación Ambiental',
            'contacto_principal': 'Lic. Lucía Quispe',
            'email_contacto': 'lquispe@conservacion.org',
            'telefono_contacto': '+51 966456123',
            'fecha_inicio': date(2023, 11, 1),
            'fecha_fin': date(2025, 10, 31),
            'objetivos': ['Conservación ambiental', 'Educación ambiental', 'Proyectos sostenibles'],
            'resultados': ['5 proyectos de conservación', '1000 personas educadas'],
            'estado': 'activa',
            'orden': 7
        },
        {
            'nombre': 'Alianza con Proveedores Locales',
            'slug': 'alianza-proveedores-locales',
            'descripcion': 'Alianza con proveedores locales de Sancos para el desarrollo económico local.',
            'tipo_alianza': 'empresa',
            'organizacion': 'Asociación de Proveedores Locales',
            'contacto_principal': 'Sr. Carlos Mendoza',
            'email_contacto': 'cmendoza@proveedoressancos.org',
            'telefono_contacto': '+51 966789456',
            'fecha_inicio': date(2023, 12, 1),
            'fecha_fin': date(2025, 11, 30),
            'objetivos': ['Desarrollo económico local', 'Cadena de suministro local', 'Capacitación empresarial'],
            'resultados': ['25 proveedores locales', 'USD 500,000 en contratos locales'],
            'estado': 'activa',
            'orden': 8
        }
    ]
    
    for alianza_data in alianzas_data:
        Alianza.objects.create(**alianza_data)
    
    # 11. Impactos Ambientales
    print("🌱 Creando impactos ambientales...")
    impactos_ambientales_data = [
        {
            'nombre': 'Programa de Reforestación Cerro San Pedro',
            'slug': 'programa-reforestacion-cerro-san-pedro',
            'descripcion_corta': 'Programa integral de reforestación en el Cerro San Pedro para restaurar la cobertura vegetal.',
            'descripcion_larga': 'Programa integral de reforestación en el Cerro San Pedro que busca restaurar la cobertura vegetal y mejorar la biodiversidad de la región.',
            'categoria': 'reforestacion',
            'ubicacion': 'Cerro San Pedro, Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2022, 1, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 500000,
            'moneda': 'USD',
            'hectareas_afectadas': 50.00,
            'especies_beneficiadas': ['Quenual', 'Chachacomo', 'Tara', 'Molle'],
            'metricas_ambientales': {
                'arboles_plantados': 25000,
                'supervivencia': '85%',
                'cobertura_vegetal': '40%'
            },
            'objetivos': ['Restaurar 50 hectáreas', 'Plantar 25,000 árboles', 'Mejorar biodiversidad'],
            'resultados': ['30 hectáreas reforestadas', '15,000 árboles plantados', 'Mejora en biodiversidad'],
            'estado': 'activo',
            'orden': 1
        },
        {
            'nombre': 'Sistema de Tratamiento de Aguas Residuales',
            'slug': 'sistema-tratamiento-aguas-residuales',
            'descripcion_corta': 'Sistema avanzado de tratamiento de aguas residuales para la planta de procesamiento.',
            'descripcion_larga': 'Sistema avanzado de tratamiento de aguas residuales que garantiza el cumplimiento de estándares ambientales y la reutilización eficiente del agua.',
            'categoria': 'agua',
            'ubicacion': 'Planta de Procesamiento, Sancos',
            'fecha_inicio': date(2021, 8, 1),
            'fecha_fin': date(2022, 6, 30),
            'presupuesto': 800000,
            'moneda': 'USD',
            'hectareas_afectadas': 5.00,
            'especies_beneficiadas': ['Peces nativos', 'Aves acuáticas', 'Vegetación ribereña'],
            'metricas_ambientales': {
                'aguas_tratadas': '100%',
                'reutilizacion': '75%',
                'calidad_agua': 'Excelente'
            },
            'objetivos': ['Tratar 100% de aguas residuales', 'Reutilizar 80% del agua', 'Cumplir estándares ambientales'],
            'resultados': ['100% de aguas tratadas', '75% de agua reutilizada', 'Cumplimiento total'],
            'estado': 'finalizado',
            'orden': 2
        },
        {
            'nombre': 'Monitoreo de Calidad del Aire',
            'slug': 'monitoreo-calidad-aire',
            'descripcion_corta': 'Sistema de monitoreo continuo de la calidad del aire en las operaciones mineras.',
            'descripcion_larga': 'Sistema de monitoreo continuo de la calidad del aire que garantiza el cumplimiento de estándares ambientales y la protección de la salud pública.',
            'categoria': 'conservacion',
            'ubicacion': 'Proyecto Rampa Nueva Jerusalén',
            'fecha_inicio': date(2022, 3, 1),
            'fecha_fin': date(2037, 12, 31),
            'presupuesto': 300000,
            'moneda': 'USD',
            'hectareas_afectadas': 100.00,
            'especies_beneficiadas': ['Aves nativas', 'Mamíferos pequeños', 'Vegetación local'],
            'metricas_ambientales': {
                'monitoreo_24h': 'Sí',
                'alertas_automaticas': 'Sí',
                'cumplimiento_estandares': '100%'
            },
            'objetivos': ['Monitoreo continuo', 'Cumplimiento de estándares', 'Alertas automáticas'],
            'resultados': ['Sistema operativo', 'Cumplimiento de estándares', 'Monitoreo 24/7'],
            'estado': 'activo',
            'orden': 3
        },
        {
            'nombre': 'Programa de Conservación de Fauna Silvestre',
            'slug': 'programa-conservacion-fauna-silvestre',
            'descripcion_corta': 'Programa de conservación y monitoreo de fauna silvestre en la zona de influencia.',
            'descripcion_larga': 'Programa integral de conservación y monitoreo de fauna silvestre que protege las especies nativas de la región de Sancos.',
            'categoria': 'biodiversidad',
            'ubicacion': 'Zona de Influencia, Sancos',
            'fecha_inicio': date(2022, 6, 1),
            'fecha_fin': date(2027, 12, 31),
            'presupuesto': 400000,
            'moneda': 'USD',
            'hectareas_afectadas': 200.00,
            'especies_beneficiadas': ['Vizcacha', 'Zorro andino', 'Cóndor', 'Aguilucho'],
            'metricas_ambientales': {
                'especies_protegidas': 5,
                'monitoreo_continuo': 'Sí',
                'educacion_ambiental': 'Sí'
            },
            'objetivos': ['Proteger especies nativas', 'Monitorear biodiversidad', 'Educar a la comunidad'],
            'resultados': ['5 especies protegidas', 'Monitoreo continuo', 'Educación ambiental'],
            'estado': 'activo',
            'orden': 4
        },
        {
            'nombre': 'Gestión Integral de Residuos Sólidos',
            'slug': 'gestion-integral-residuos-solidos',
            'descripcion_corta': 'Programa integral de gestión de residuos sólidos con reciclaje y reutilización.',
            'descripcion_larga': 'Programa integral de gestión de residuos sólidos que implementa reciclaje, reutilización y reducción de residuos en todas las operaciones.',
            'categoria': 'gestion_residuos',
            'ubicacion': 'Campamento Minero, Sancos',
            'fecha_inicio': date(2022, 1, 1),
            'fecha_fin': date(2037, 12, 31),
            'presupuesto': 200000,
            'moneda': 'USD',
            'hectareas_afectadas': 10.00,
            'especies_beneficiadas': ['Aves carroñeras', 'Insectos descomponedores'],
            'metricas_ambientales': {
                'residuos_reciclados': '55%',
                'reduccion_residuos': '45%',
                'personal_capacitado': '100%'
            },
            'objetivos': ['Reciclar 60% de residuos', 'Reducir residuos al 50%', 'Educar personal'],
            'resultados': ['55% de residuos reciclados', '45% de reducción', 'Personal capacitado'],
            'estado': 'activo',
            'orden': 5
        },
        {
            'nombre': 'Programa de Eficiencia Energética',
            'slug': 'programa-eficiencia-energetica',
            'descripcion_corta': 'Programa de optimización energética y reducción de emisiones de gases de efecto invernadero.',
            'descripcion_larga': 'Programa de optimización energética que reduce las emisiones de gases de efecto invernadero y mejora la eficiencia operacional.',
            'categoria': 'energia_renovable',
            'ubicacion': 'Todas las operaciones',
            'fecha_inicio': date(2022, 9, 1),
            'fecha_fin': date(2025, 12, 31),
            'presupuesto': 600000,
            'moneda': 'USD',
            'hectareas_afectadas': 500.00,
            'especies_beneficiadas': ['Todas las especies locales'],
            'metricas_ambientales': {
                'reduccion_energetica': '20%',
                'reduccion_emisiones': '25%',
                'sistema_solar': 'Instalado'
            },
            'objetivos': ['Reducir 25% consumo energético', 'Reducir 30% emisiones', 'Implementar energías renovables'],
            'resultados': ['20% de reducción energética', '25% de reducción emisiones', 'Sistema solar instalado'],
            'estado': 'activo',
            'orden': 6
        },
        {
            'nombre': 'Restauración de Suelos Degradados',
            'slug': 'restauracion-suelos-degradados',
            'descripcion_corta': 'Programa de restauración de suelos degradados por actividades mineras.',
            'descripcion_larga': 'Programa integral de restauración de suelos degradados que mejora la fertilidad y establece cobertura vegetal sostenible.',
            'categoria': 'conservacion',
            'ubicacion': 'Áreas de Influencia, Sancos',
            'fecha_inicio': date(2023, 1, 1),
            'fecha_fin': date(2026, 12, 31),
            'presupuesto': 350000,
            'moneda': 'USD',
            'hectareas_afectadas': 20.00,
            'especies_beneficiadas': ['Vegetación nativa', 'Microorganismos del suelo'],
            'metricas_ambientales': {
                'suelos_restaurados': 10,
                'mejora_fertilidad': 'Sí',
                'cobertura_vegetal': 'Establecida'
            },
            'objetivos': ['Restaurar 20 hectáreas', 'Mejorar fertilidad del suelo', 'Establecer cobertura vegetal'],
            'resultados': ['10 hectáreas restauradas', 'Mejora en fertilidad', 'Cobertura vegetal establecida'],
            'estado': 'activo',
            'orden': 7
        },
        {
            'nombre': 'Programa de Educación Ambiental',
            'slug': 'programa-educacion-ambiental',
            'descripcion_corta': 'Programa de educación ambiental para la comunidad de Sancos y personal de la empresa.',
            'descripcion_larga': 'Programa integral de educación ambiental que crea conciencia sobre la importancia de la conservación y las prácticas sostenibles.',
            'categoria': 'educacion_ambiental',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'fecha_inicio': date(2022, 3, 1),
            'fecha_fin': date(2037, 12, 31),
            'presupuesto': 150000,
            'moneda': 'USD',
            'hectareas_afectadas': 1000.00,
            'especies_beneficiadas': ['Todas las especies de la región'],
            'metricas_ambientales': {
                'personas_educadas': 300,
                'conciencia_ambiental': 'Creada',
                'practicas_sostenibles': 'Implementadas'
            },
            'objetivos': ['Educar 500 personas', 'Crear conciencia ambiental', 'Promover prácticas sostenibles'],
            'resultados': ['300 personas educadas', 'Conciencia ambiental creada', 'Prácticas implementadas'],
            'estado': 'activo',
            'orden': 8
        }
    ]
    
    for impacto_data in impactos_ambientales_data:
        ImpactoAmbiental.objects.create(**impacto_data)
    
    # 12. Reportes de Sostenibilidad
    print("📊 Creando reportes de sostenibilidad...")
    reportes_data = [
        {
            'titulo': 'Reporte de Sostenibilidad 2023',
            'slug': 'reporte-sostenibilidad-2023',
            'descripcion': 'Reporte anual de sostenibilidad 2023 con información completa sobre el desempeño ambiental, social y económico.',
            'año': 2023,
            'tipo_reporte': 'sostenibilidad',
            'resumen_ejecutivo': 'Nuestro compromiso con la sostenibilidad y el desarrollo responsable se refleja en este reporte anual.',
            'indicadores_clave': {
                'reduccion_emisiones': '25%',
                'personas_capacitadas': 300,
                'inversion_social': 'USD 2.5M'
            },
            'logros_principales': ['25% reducción de emisiones', '300 personas capacitadas', 'USD 2.5M en inversión social'],
            'desafios': ['Continuar reduciendo emisiones', 'Ampliar programas sociales', 'Mejorar eficiencia energética'],
            'fecha_publicacion': date(2024, 3, 15),
            'estado': 'publicado',
            'orden': 1
        },
        {
            'titulo': 'Reporte de Impacto Social 2023',
            'slug': 'reporte-impacto-social-2023',
            'descripcion': 'Reporte específico sobre el impacto social de las operaciones en la comunidad de Sancos.',
            'año': 2023,
            'tipo_reporte': 'responsabilidad_social',
            'resumen_ejecutivo': 'Análisis detallado del impacto social de nuestras operaciones en la comunidad de Sancos.',
            'indicadores_clave': {
                'empleos_generados': 200,
                'familias_beneficiadas': 500,
                'programas_sociales': 8
            },
            'logros_principales': ['200 empleos generados', '500 familias beneficiadas', '8 programas sociales'],
            'desafios': ['Ampliar cobertura de programas', 'Mejorar indicadores sociales', 'Fortalecer relaciones comunitarias'],
            'fecha_publicacion': date(2024, 2, 28),
            'estado': 'publicado',
            'orden': 2
        },
        {
            'titulo': 'Reporte Ambiental 2023',
            'slug': 'reporte-ambiental-2023',
            'descripcion': 'Reporte detallado sobre el desempeño ambiental y las iniciativas de conservación.',
            'año': 2023,
            'tipo_reporte': 'ambiental',
            'resumen_ejecutivo': 'Evaluación completa del desempeño ambiental y las iniciativas de conservación implementadas.',
            'indicadores_clave': {
                'aguas_tratadas': '100%',
                'residuos_reciclados': '55%',
                'arboles_plantados': 15000
            },
            'logros_principales': ['100% de aguas tratadas', '55% de residuos reciclados', '15,000 árboles plantados'],
            'desafios': ['Aumentar reciclaje', 'Reducir huella de carbono', 'Mejorar biodiversidad'],
            'fecha_publicacion': date(2024, 3, 10),
            'estado': 'publicado',
            'orden': 3
        },
        {
            'titulo': 'Reporte de Seguridad y Salud Ocupacional 2023',
            'slug': 'reporte-seguridad-salud-2023',
            'descripcion': 'Reporte sobre el desempeño en seguridad y salud ocupacional de las operaciones mineras.',
            'año': 2023,
            'tipo_reporte': 'responsabilidad_social',
            'resumen_ejecutivo': 'Análisis del desempeño en seguridad y salud ocupacional de nuestras operaciones.',
            'indicadores_clave': {
                'accidentes_fatales': 0,
                'incidentes_menores': 5,
                'horas_trabajadas': 500000
            },
            'logros_principales': ['Cero accidentes fatales', 'Reducción de incidentes', 'Mejora en indicadores'],
            'desafios': ['Mantener cero accidentes', 'Mejorar cultura de seguridad', 'Reducir incidentes menores'],
            'fecha_publicacion': date(2024, 2, 15),
            'estado': 'publicado',
            'orden': 4
        },
        {
            'titulo': 'Reporte de Innovación y Tecnología 2023',
            'slug': 'reporte-innovacion-tecnologia-2023',
            'descripcion': 'Reporte sobre las iniciativas de innovación y desarrollo tecnológico implementadas.',
            'año': 2023,
            'tipo_reporte': 'sostenibilidad',
            'resumen_ejecutivo': 'Revisión de las iniciativas de innovación y desarrollo tecnológico implementadas.',
            'indicadores_clave': {
                'patentes_registradas': 8,
                'proyectos_innovacion': 8,
                'tecnologias_implementadas': 8
            },
            'logros_principales': ['8 patentes registradas', '8 proyectos de innovación', '8 tecnologías implementadas'],
            'desafios': ['Aumentar innovación', 'Desarrollar más patentes', 'Implementar nuevas tecnologías'],
            'fecha_publicacion': date(2024, 3, 20),
            'estado': 'publicado',
            'orden': 5
        },
        {
            'titulo': 'Reporte de Gestión de Residuos 2023',
            'slug': 'reporte-gestion-residuos-2023',
            'descripcion': 'Reporte específico sobre la gestión integral de residuos y cumplimiento ambiental.',
            'año': 2023,
            'tipo_reporte': 'ambiental',
            'resumen_ejecutivo': 'Evaluación de la gestión integral de residuos y cumplimiento ambiental.',
            'indicadores_clave': {
                'residuos_generados': '1000 ton',
                'residuos_reciclados': '550 ton',
                'reduccion_residuos': '45%'
            },
            'logros_principales': ['55% de residuos reciclados', '45% de reducción', 'Cumplimiento ambiental'],
            'desafios': ['Aumentar reciclaje', 'Reducir generación', 'Mejorar gestión'],
            'fecha_publicacion': date(2024, 3, 5),
            'estado': 'publicado',
            'orden': 6
        },
        {
            'titulo': 'Reporte de Desarrollo Comunitario 2023',
            'slug': 'reporte-desarrollo-comunitario-2023',
            'descripcion': 'Reporte sobre los programas de desarrollo comunitario implementados en Sancos.',
            'año': 2023,
            'tipo_reporte': 'responsabilidad_social',
            'resumen_ejecutivo': 'Análisis de los programas de desarrollo comunitario implementados en Sancos.',
            'indicadores_clave': {
                'programas_implementados': 8,
                'beneficiarios_directos': 1500,
                'inversion_comunitaria': 'USD 2.3M'
            },
            'logros_principales': ['8 programas implementados', '1,500 beneficiarios directos', 'USD 2.3M invertidos'],
            'desafios': ['Ampliar programas', 'Aumentar beneficiarios', 'Mejorar impacto'],
            'fecha_publicacion': date(2024, 2, 20),
            'estado': 'publicado',
            'orden': 7
        },
        {
            'titulo': 'Reporte de Cumplimiento Normativo 2023',
            'slug': 'reporte-cumplimiento-normativo-2023',
            'descripcion': 'Reporte sobre el cumplimiento de todas las normativas ambientales, sociales y laborales.',
            'año': 2023,
            'tipo_reporte': 'sostenibilidad',
            'resumen_ejecutivo': 'Evaluación del cumplimiento de todas las normativas aplicables.',
            'indicadores_clave': {
                'normativas_cumplidas': '100%',
                'auditorias_exitosas': 15,
                'certificaciones_mantenidas': 8
            },
            'logros_principales': ['100% de normativas cumplidas', '15 auditorías exitosas', '8 certificaciones mantenidas'],
            'desafios': ['Mantener cumplimiento', 'Mejorar estándares', 'Obtener nuevas certificaciones'],
            'fecha_publicacion': date(2024, 3, 25),
            'estado': 'publicado',
            'orden': 8
        }
    ]
    
    for reporte_data in reportes_data:
        ReporteSostenibilidad.objects.create(**reporte_data)
    
    # 13. Categorías de Blog
    print("📰 Creando categorías de blog...")
    categorias_blog = [
        {'nombre': 'Tecnología Minera', 'descripcion': 'Artículos sobre tecnología en minería'},
        {'nombre': 'Sostenibilidad', 'descripcion': 'Artículos sobre sostenibilidad y medio ambiente'},
        {'nombre': 'Innovación', 'descripcion': 'Artículos sobre innovación en minería'},
        {'nombre': 'Responsabilidad Social', 'descripcion': 'Artículos sobre responsabilidad social'},
    ]
    
    for cat_data in categorias_blog:
        CategoriaBlog.objects.create(**cat_data)
    
    # 14. Equipo (mover antes de las noticias)
    print("👥 Creando equipo...")
    equipo_data = [
        {
            'nombre': 'Juan Carlos',
            'apellido': 'Rodríguez',
            'cargo': 'Director General',
            'departamento': 'Dirección',
            'biografia': 'Ingeniero de minas con más de 20 años de experiencia en minería subterránea. Lidera las operaciones de Minera Fidami S.A. en el proyecto Rampa Nueva Jerusalén.',
            'email': 'jrodriguez@minerafidami.com.pe',
            'linkedin_url': 'https://linkedin.com/in/juan-rodriguez',
            'experiencia_anos': 20,
            'educacion': ['Ingeniería de Minas - Universidad Nacional de Ingeniería'],
            'especialidades': ['Minería subterránea', 'Gestión de proyectos', 'Seguridad minera'],
            'certificaciones': ['Certificación en Seguridad Minera', 'ISO 14001'],
            'directivo': True,
            'orden': 1,
            'estado': 'activo'
        },
        {
            'nombre': 'María Elena',
            'apellido': 'López',
            'cargo': 'Gerente de Operaciones',
            'departamento': 'Operaciones',
            'biografia': 'Ingeniera industrial especializada en optimización de procesos mineros. Supervisa las operaciones de la planta de procesamiento en Sancos.',
            'email': 'mlopez@minerafidami.com.pe',
            'linkedin_url': 'https://linkedin.com/in/maria-lopez',
            'experiencia_anos': 15,
            'educacion': ['Ingeniería Industrial - Universidad de Lima'],
            'especialidades': ['Optimización de procesos', 'Gestión de calidad', 'Lean Six Sigma'],
            'certificaciones': ['Lean Six Sigma Black Belt', 'ISO 9001'],
            'directivo': True,
            'orden': 2,
            'estado': 'activo'
        },
        {
            'nombre': 'Carlos',
            'apellido': 'Mendoza',
            'cargo': 'Superintendente de Mina',
            'departamento': 'Operaciones',
            'biografia': 'Ingeniero de minas con amplia experiencia en minería subterránea. Responsable de las operaciones de extracción en el proyecto Rampa Nueva Jerusalén.',
            'email': 'cmendoza@minerafidami.com.pe',
            'linkedin_url': 'https://linkedin.com/in/carlos-mendoza',
            'experiencia_anos': 12,
            'educacion': ['Ingeniería de Minas - Universidad Nacional de San Agustín'],
            'especialidades': ['Minería subterránea', 'Ventilación minera', 'Geomecánica'],
            'certificaciones': ['Supervisor de Seguridad Minera', 'Ventilación Minera'],
            'directivo': False,
            'orden': 3,
            'estado': 'activo'
        },
        {
            'nombre': 'Ana',
            'apellido': 'Torres',
            'cargo': 'Jefa de Planta',
            'departamento': 'Procesamiento',
            'biografia': 'Ingeniera metalúrgica especializada en procesamiento de minerales auríferos. Supervisa la operación de la planta de procesamiento de 500 TPD.',
            'email': 'atorres@minerafidami.com.pe',
            'linkedin_url': 'https://linkedin.com/in/ana-torres',
            'experiencia_anos': 10,
            'educacion': ['Ingeniería Metalúrgica - Universidad Nacional de Ingeniería'],
            'especialidades': ['Procesamiento de oro', 'Cianuración', 'Control de calidad'],
            'certificaciones': ['Auditora ISO 9001', 'Gestión de Calidad'],
            'directivo': False,
            'orden': 4,
            'estado': 'activo'
        },
        {
            'nombre': 'Roberto',
            'apellido': 'Vargas',
            'cargo': 'Supervisor de Seguridad',
            'departamento': 'Seguridad',
            'biografia': 'Técnico en seguridad minera con amplia experiencia en implementación de sistemas de gestión de seguridad. Responsable de la seguridad en todas las operaciones.',
            'email': 'rvargas@minerafidami.com.pe',
            'linkedin_url': 'https://linkedin.com/in/roberto-vargas',
            'experiencia_anos': 8,
            'educacion': ['Técnico en Seguridad Minera - SENATI'],
            'especialidades': ['Seguridad minera', 'Gestión de riesgos', 'Capacitación'],
            'certificaciones': ['Supervisor de Seguridad Minera', 'ISO 45001'],
            'directivo': False,
            'orden': 5,
            'estado': 'activo'
        },
        {
            'nombre': 'Lucía',
            'apellido': 'Quispe',
            'cargo': 'Responsable de Relaciones Comunitarias',
            'departamento': 'Sostenibilidad',
            'biografia': 'Profesional en relaciones comunitarias con experiencia en desarrollo sostenible. Coordina los programas de desarrollo comunitario en Sancos.',
            'email': 'lquispe@minerafidami.com.pe',
            'linkedin_url': 'https://linkedin.com/in/lucia-quispe',
            'experiencia_anos': 6,
            'educacion': ['Sociología - Universidad Nacional de San Cristóbal de Huamanga'],
            'especialidades': ['Relaciones comunitarias', 'Desarrollo sostenible', 'Responsabilidad social'],
            'certificaciones': ['Gestión de Relaciones Comunitarias'],
            'directivo': False,
            'orden': 6,
            'estado': 'activo'
        }
    ]
    
    for miembro_data in equipo_data:
        Equipo.objects.create(**miembro_data)
    
    # 15. Noticias del Blog
    print("📝 Creando noticias del blog...")
    from datetime import datetime
    noticias_data = [
        {
            'titulo': 'Minera Fidami S.A. Inicia Operaciones en Proyecto Rampa Nueva Jerusalén',
            'slug': 'minera-fidami-inicia-operaciones-rampa-nueva-jerusalen',
            'resumen': 'Minera Fidami S.A. anuncia el inicio oficial de operaciones en el proyecto Rampa Nueva Jerusalén, ubicado en Sancos, Lucanas, Ayacucho.',
            'contenido': '''
            <h2>Inicio de Operaciones en Sancos</h2>
            <p>Minera Fidami S.A. se complace en anunciar el inicio oficial de operaciones en el proyecto Rampa Nueva Jerusalén, ubicado en el distrito de Sancos, provincia de Lucanas, departamento de Ayacucho. Este hito representa un importante paso en el desarrollo de la minería subterránea en la región.</p>
            
            <h3>Características del Proyecto</h3>
            <ul>
                <li><strong>Ubicación:</strong> Sancos, Lucanas, Ayacucho</li>
                <li><strong>Tipo de Operación:</strong> Minería subterránea de oro</li>
                <li><strong>Capacidad de Procesamiento:</strong> 500 toneladas por día</li>
                <li><strong>Vida Útil Estimada:</strong> 15 años</li>
                <li><strong>Ley Promedio:</strong> 8.5 g/t Au</li>
            </ul>
            
            <h3>Beneficios para la Comunidad</h3>
            <p>El proyecto generará empleo directo e indirecto para la comunidad de Sancos, contribuyendo al desarrollo económico de la región. Además, se implementarán programas de desarrollo comunitario y responsabilidad social.</p>
            
            <h3>Compromiso Ambiental</h3>
            <p>Minera Fidami S.A. opera bajo los más altos estándares de protección ambiental, implementando tecnologías de vanguardia para minimizar el impacto en el entorno natural.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Responsabilidad Social'),
            'autor': Equipo.objects.get(nombre='Juan Carlos'),
            'fecha_publicacion': datetime(2023, 12, 15, 10, 0, 0),
            'estado': 'publicado',
            'destacado': True,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Innovaciones Tecnológicas en Minería Subterránea',
            'slug': 'innovaciones-tecnologicas-mineria-subterranea',
            'resumen': 'Descubre las últimas innovaciones tecnológicas implementadas en las operaciones de minería subterránea de Minera Fidami S.A.',
            'contenido': '''
            <h2>Innovación en Minería Subterránea</h2>
            <p>Minera Fidami S.A. continúa liderando la innovación en minería subterránea con la implementación de tecnologías de vanguardia en el proyecto Rampa Nueva Jerusalén.</p>
            
            <h3>Sistema de Ventilación Inteligente</h3>
            <p>Hemos implementado un sistema de ventilación subterránea con control automático y monitoreo en tiempo real de gases y calidad del aire, mejorando significativamente la seguridad operacional.</p>
            
            <h3>Perforación Automatizada</h3>
            <p>Los equipos de perforación con control automático y GPS subterráneo permiten mayor precisión y eficiencia en el desarrollo de túneles y rampas.</p>
            
            <h3>Monitoreo Geotécnico en Tiempo Real</h3>
            <p>Sistema de sensores y monitoreo continuo de la estabilidad de taludes y estructuras subterráneas, previniendo riesgos geotécnicos.</p>
            
            <h3>Beneficios de la Innovación</h3>
            <ul>
                <li>Mayor seguridad operacional</li>
                <li>Incremento en la productividad</li>
                <li>Reducción de costos operativos</li>
                <li>Mejora en la calidad del producto final</li>
            </ul>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Tecnología Minera'),
            'autor': Equipo.objects.get(nombre='María Elena'),
            'fecha_publicacion': datetime(2023, 12, 10, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Programa de Desarrollo Comunitario en Sancos',
            'slug': 'programa-desarrollo-comunitario-sancos',
            'resumen': 'Conoce los programas de desarrollo comunitario implementados por Minera Fidami S.A. en la comunidad de Sancos.',
            'contenido': '''
            <h2>Desarrollo Comunitario en Sancos</h2>
            <p>Minera Fidami S.A. ha implementado un programa integral de desarrollo comunitario en el distrito de Sancos, provincia de Lucanas, Ayacucho, contribuyendo al desarrollo sostenible de la región.</p>
            
            <h3>Programas Implementados</h3>
            <ul>
                <li><strong>Educación Integral:</strong> Mejora de infraestructura educativa y capacitación docente</li>
                <li><strong>Salud Comunitaria:</strong> Atención médica preventiva y curativa</li>
                <li><strong>Desarrollo Económico:</strong> Apoyo a emprendimientos locales</li>
                <li><strong>Infraestructura Rural:</strong> Mejora de caminos y sistemas de agua</li>
            </ul>
            
            <h3>Resultados Alcanzados</h3>
            <ul>
                <li>150 estudiantes beneficiados en educación</li>
                <li>500 familias atendidas en salud</li>
                <li>25 nuevos empleos locales creados</li>
                <li>15 km de caminos mejorados</li>
            </ul>
            
            <h3>Compromiso Continuo</h3>
            <p>Minera Fidami S.A. mantiene un compromiso firme con el desarrollo sostenible de la comunidad de Sancos, trabajando de manera colaborativa con las autoridades locales y la población.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Responsabilidad Social'),
            'autor': Equipo.objects.get(nombre='Lucía'),
            'fecha_publicacion': datetime(2023, 11, 25, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Optimización de Procesamiento de Oro',
            'slug': 'optimizacion-procesamiento-oro',
            'resumen': 'Minera Fidami S.A. implementa nuevas tecnologías para optimizar el procesamiento de oro en su planta de 500 TPD.',
            'contenido': '''
            <h2>Optimización de Procesos</h2>
            <p>Minera Fidami S.A. ha implementado nuevas tecnologías para optimizar el procesamiento de oro en su planta de 500 toneladas por día, logrando una recuperación del 95%.</p>
            
            <h3>Tecnologías Implementadas</h3>
            <ul>
                <li><strong>Flotación Selectiva:</strong> Separación eficiente de minerales auríferos</li>
                <li><strong>Cianuración Optimizada:</strong> Proceso mejorado de lixiviación</li>
                <li><strong>Carbón Activado:</strong> Recuperación eficiente de oro</li>
                <li><strong>Control Automatizado:</strong> Sistema SCADA para optimización</li>
            </ul>
            
            <h3>Resultados Alcanzados</h3>
            <ul>
                <li>Recuperación del 95% de oro</li>
                <li>Reducción del 15% en consumo de reactivos</li>
                <li>Mejora en la calidad del producto final</li>
                <li>Optimización energética del 20%</li>
            </ul>
            
            <h3>Beneficios Ambientales</h3>
            <p>Las nuevas tecnologías también contribuyen a reducir el impacto ambiental, optimizando el uso de agua y reactivos químicos.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Tecnología Minera'),
            'autor': Equipo.objects.get(nombre='Ana'),
            'fecha_publicacion': datetime(2023, 11, 15, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Seguridad Minera: Prioridad en Minera Fidami S.A.',
            'slug': 'seguridad-minera-prioridad-minera-fidami',
            'resumen': 'La seguridad es el pilar fundamental de las operaciones de Minera Fidami S.A. Conoce nuestras iniciativas de seguridad.',
            'contenido': '''
            <h2>Seguridad: Nuestro Pilar Fundamental</h2>
            <p>En Minera Fidami S.A., la seguridad es el pilar fundamental de todas nuestras operaciones. Implementamos sistemas avanzados y capacitación continua para garantizar la seguridad de nuestro personal.</p>
            
            <h3>Sistemas de Seguridad Implementados</h3>
            <ul>
                <li><strong>Monitoreo de Gases:</strong> Sensores de CO, NOx, SO2 y partículas</li>
                <li><strong>Ventilación Inteligente:</strong> Control automático de calidad del aire</li>
                <li><strong>Monitoreo Geotécnico:</strong> Sensores de estabilidad de taludes</li>
                <li><strong>Equipos de Protección:</strong> EPP de última generación</li>
            </ul>
            
            <h3>Capacitación Continua</h3>
            <p>Implementamos programas de capacitación continua en seguridad para todo el personal, incluyendo:</p>
            <ul>
                <li>Capacitación en primeros auxilios</li>
                <li>Entrenamiento en uso de equipos de seguridad</li>
                <li>Simulacros de emergencia</li>
                <li>Actualización de procedimientos de seguridad</li>
            </ul>
            
            <h3>Resultados de Seguridad</h3>
            <p>Nuestro compromiso con la seguridad se refleja en nuestros indicadores: cero accidentes fatales y reducción continua de incidentes menores.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Responsabilidad Social'),
            'autor': Equipo.objects.get(nombre='Roberto'),
            'fecha_publicacion': datetime(2023, 11, 5, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Exploración Geológica en Cerro San Pedro',
            'slug': 'exploracion-geologica-cerro-san-pedro',
            'resumen': 'Minera Fidami S.A. inicia programa de exploración geológica en el Cerro San Pedro, Sancos.',
            'contenido': '''
            <h2>Exploración en Cerro San Pedro</h2>
            <p>Minera Fidami S.A. ha iniciado un programa de exploración geológica en el Cerro San Pedro, ubicado en el distrito de Sancos, provincia de Lucanas, Ayacucho.</p>
            
            <h3>Actividades de Exploración</h3>
            <ul>
                <li><strong>Mapeo Geológico:</strong> Cartografía detallada de la geología superficial</li>
                <li><strong>Perforación Diamantina:</strong> 5,000 metros de perforación planificados</li>
                <li><strong>Análisis Geoquímicos:</strong> Muestreo sistemático de suelos y rocas</li>
                <li><strong>Geofísica:</strong> Estudios de resistividad y polarización inducida</li>
            </ul>
            
            <h3>Resultados Preliminares</h3>
            <ul>
                <li>Área de interés: 2,500 hectáreas</li>
                <li>3 zonas anómalas identificadas</li>
                <li>Leyes promedio: 3.2 g/t Au en muestras de superficie</li>
                <li>Profundidad investigada: hasta 200 metros</li>
            </ul>
            
            <h3>Próximos Pasos</h3>
            <p>El programa de exploración continuará con la expansión de la perforación diamantina y la evaluación económica preliminar de los resultados obtenidos.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Tecnología Minera'),
            'autor': Equipo.objects.get(nombre='Carlos'),
            'fecha_publicacion': datetime(2023, 10, 25, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Gestión Ambiental en Minería Subterránea',
            'slug': 'gestion-ambiental-mineria-subterranea',
            'resumen': 'Conoce las iniciativas de gestión ambiental implementadas por Minera Fidami S.A. en sus operaciones subterráneas.',
            'contenido': '''
            <h2>Gestión Ambiental Integral</h2>
            <p>Minera Fidami S.A. implementa un sistema integral de gestión ambiental en sus operaciones subterráneas, minimizando el impacto en el entorno natural.</p>
            
            <h3>Iniciativas Ambientales</h3>
            <ul>
                <li><strong>Tratamiento de Aguas:</strong> Sistema avanzado de tratamiento de aguas residuales</li>
                <li><strong>Gestión de Residuos:</strong> Reciclaje y reutilización de residuos sólidos</li>
                <li><strong>Eficiencia Energética:</strong> Optimización del consumo energético</li>
                <li><strong>Conservación de Biodiversidad:</strong> Protección de especies nativas</li>
            </ul>
            
            <h3>Resultados Ambientales</h3>
            <ul>
                <li>100% de aguas residuales tratadas</li>
                <li>75% de agua reutilizada en procesos</li>
                <li>55% de residuos reciclados</li>
                <li>25% de reducción en emisiones</li>
            </ul>
            
            <h3>Compromiso Continuo</h3>
            <p>Minera Fidami S.A. mantiene un compromiso firme con la protección ambiental, implementando las mejores prácticas y tecnologías disponibles.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Responsabilidad Social'),
            'autor': Equipo.objects.get(nombre='María Elena'),
            'fecha_publicacion': datetime(2023, 10, 15, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        },
        {
            'titulo': 'Capacitación y Desarrollo del Personal',
            'slug': 'capacitacion-desarrollo-personal',
            'resumen': 'Minera Fidami S.A. invierte en la capacitación y desarrollo profesional de su personal.',
            'contenido': '''
            <h2>Desarrollo Profesional Continuo</h2>
            <p>Minera Fidami S.A. reconoce que su mayor activo es su personal. Por ello, implementamos programas integrales de capacitación y desarrollo profesional.</p>
            
            <h3>Programas de Capacitación</h3>
            <ul>
                <li><strong>Capacitación Técnica:</strong> Entrenamiento en equipos especializados</li>
                <li><strong>Desarrollo de Competencias:</strong> Programas de liderazgo y gestión</li>
                <li><strong>Seguridad Minera:</strong> Capacitación continua en seguridad</li>
                <li><strong>Nuevas Tecnologías:</strong> Actualización en tecnologías mineras</li>
            </ul>
            
            <h3>Beneficios para el Personal</h3>
            <ul>
                <li>Mejora de competencias técnicas</li>
                <li>Oportunidades de crecimiento profesional</li>
                <li>Mayor empleabilidad</li>
                <li>Desarrollo de habilidades de liderazgo</li>
            </ul>
            
            <h3>Resultados Alcanzados</h3>
            <p>Nuestros programas de capacitación han resultado en una mejora significativa en la productividad y satisfacción del personal, contribuyendo al éxito de nuestras operaciones.</p>
            ''',
            'categoria': CategoriaBlog.objects.get(nombre='Responsabilidad Social'),
            'autor': Equipo.objects.get(nombre='Juan Carlos'),
            'fecha_publicacion': datetime(2023, 10, 5, 10, 0, 0),
            'estado': 'publicado',
            'destacado': False,
            'imagen_principal_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800'
        }
    ]
    
    for noticia_data in noticias_data:
        NoticiaBlog.objects.create(**noticia_data)
    
    # 16. Vacantes
    print("💼 Creando vacantes...")
    vacantes_data = [
        {
            'titulo': 'Ingeniero de Minas Senior',
            'slug': 'ingeniero-minas-senior',
            'descripcion': 'Buscamos un Ingeniero de Minas Senior con experiencia en minería subterránea para liderar operaciones mineras.',
            'requisitos': ['Ingeniería de Minas', '5+ años de experiencia', 'Conocimiento en minería subterránea'],
            'responsabilidades': ['Liderar operaciones mineras', 'Supervisar equipos', 'Optimizar procesos'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación continua'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Operaciones',
            'experiencia_minima': 5,
            'experiencia_maxima': 10,
            'salario_min': 5000,
            'salario_max': 8000,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': True
        },
        {
            'titulo': 'Geólogo de Exploración',
            'slug': 'geologo-exploracion',
            'descripcion': 'Geólogo especializado en exploración minera para identificar nuevos yacimientos.',
            'requisitos': ['Geología', '3+ años de experiencia', 'Conocimiento en exploración'],
            'responsabilidades': ['Mapeo geológico', 'Análisis de muestras', 'Reportes técnicos'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Geología',
            'experiencia_minima': 3,
            'experiencia_maxima': 7,
            'salario_min': 4000,
            'salario_max': 6000,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': False
        },
        {
            'titulo': 'Supervisor de Seguridad',
            'slug': 'supervisor-seguridad',
            'descripcion': 'Supervisor de seguridad para garantizar el cumplimiento de estándares de seguridad minera.',
            'requisitos': ['Ingeniería Industrial', '4+ años de experiencia', 'Certificación en seguridad'],
            'responsabilidades': ['Supervisar protocolos de seguridad', 'Capacitar personal', 'Investigación de incidentes'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Seguridad',
            'experiencia_minima': 4,
            'experiencia_maxima': 8,
            'salario_min': 4500,
            'salario_max': 7000,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': True
        },
        {
            'titulo': 'Operador de Equipos Pesados',
            'slug': 'operador-equipos-pesados',
            'descripcion': 'Operador de equipos pesados para operaciones mineras subterráneas.',
            'requisitos': ['Licencia de conducir', '2+ años de experiencia', 'Conocimiento de equipos'],
            'responsabilidades': ['Operar equipos pesados', 'Mantenimiento preventivo', 'Reportes diarios'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Operaciones',
            'experiencia_minima': 2,
            'experiencia_maxima': 5,
            'salario_min': 2500,
            'salario_max': 4000,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': False
        },
        {
            'titulo': 'Técnico de Laboratorio',
            'slug': 'tecnico-laboratorio',
            'descripcion': 'Técnico de laboratorio para análisis de muestras minerales.',
            'requisitos': ['Técnico en laboratorio', '1+ años de experiencia', 'Conocimiento en análisis'],
            'responsabilidades': ['Análisis de muestras', 'Mantenimiento de equipos', 'Reportes técnicos'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Laboratorio',
            'experiencia_minima': 1,
            'experiencia_maxima': 3,
            'salario_min': 2000,
            'salario_max': 3500,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': False
        },
        {
            'titulo': 'Ingeniero Ambiental',
            'slug': 'ingeniero-ambiental',
            'descripcion': 'Ingeniero ambiental para gestionar el cumplimiento ambiental de las operaciones.',
            'requisitos': ['Ingeniería Ambiental', '3+ años de experiencia', 'Conocimiento en gestión ambiental'],
            'responsabilidades': ['Gestión ambiental', 'Cumplimiento normativo', 'Reportes ambientales'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Ambiente',
            'experiencia_minima': 3,
            'experiencia_maxima': 6,
            'salario_min': 4000,
            'salario_max': 6000,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': False
        },
        {
            'titulo': 'Mecánico de Equipos Mineros',
            'slug': 'mecanico-equipos-mineros',
            'descripcion': 'Mecánico especializado en equipos mineros para mantenimiento y reparación.',
            'requisitos': ['Técnico mecánico', '3+ años de experiencia', 'Conocimiento de equipos mineros'],
            'responsabilidades': ['Mantenimiento de equipos', 'Reparaciones', 'Prevención de fallas'],
            'beneficios': ['Salario competitivo', 'Seguro médico', 'Capacitación'],
            'tipo_contrato': 'tiempo_completo',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Mantenimiento',
            'experiencia_minima': 3,
            'experiencia_maxima': 7,
            'salario_min': 3000,
            'salario_max': 5000,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': False
        },
        {
            'titulo': 'Practicante de Ingeniería',
            'slug': 'practicante-ingenieria',
            'descripcion': 'Práctica profesional para estudiantes de ingeniería en sus últimos años.',
            'requisitos': ['Estudiante de ingeniería', 'Últimos años', 'Disposición para aprender'],
            'responsabilidades': ['Apoyo en proyectos', 'Análisis de datos', 'Reportes técnicos'],
            'beneficios': ['Capacitación', 'Experiencia práctica', 'Posibilidad de contratación'],
            'tipo_contrato': 'practicas',
            'ubicacion': 'Sancos, Lucanas, Ayacucho',
            'departamento': 'Varios',
            'experiencia_minima': 0,
            'experiencia_maxima': 1,
            'salario_min': 800,
            'salario_max': 1200,
            'moneda': 'USD',
            'fecha_limite': date(2024, 12, 31),
            'estado': 'abierta',
            'destacada': False
        }
    ]
    
    for vacante_data in vacantes_data:
        Vacante.objects.create(**vacante_data)
    
    # 17. Testimonios
    print("💬 Creando testimonios...")
    testimonios_data = [
        {
            'nombre': 'María Quispe',
            'cargo': 'Presidenta de la Comunidad',
            'empresa': 'Comunidad Campesina de Sancos',
            'testimonio': 'Minera Fidami S.A. ha transformado positivamente nuestra comunidad. Han generado empleo local, mejorado nuestras escuelas y apoyado nuestros proyectos de desarrollo. Su compromiso con la responsabilidad social es genuino.',
            'calificacion': 5,
            'proyecto_relacionado': 'Desarrollo Comunitario Sancos',
            'estado': 'activo',
            'destacado': True,
            'orden': 1
        },
        {
            'nombre': 'Carlos Mendoza',
            'cargo': 'Superintendente de Mina',
            'empresa': 'Minera Fidami S.A.',
            'testimonio': 'Trabajar en el proyecto Rampa Nueva Jerusalén ha sido una experiencia excepcional. La empresa prioriza la seguridad y el desarrollo profesional de su personal. Las operaciones subterráneas están a la vanguardia de la tecnología minera.',
            'calificacion': 5,
            'proyecto_relacionado': 'Proyecto Rampa Nueva Jerusalén',
            'estado': 'activo',
            'destacado': True,
            'orden': 2
        },
        {
            'nombre': 'Ana Torres',
            'cargo': 'Jefa de Planta',
            'empresa': 'Minera Fidami S.A.',
            'testimonio': 'La planta de procesamiento de minerales opera con tecnología de punta y estándares internacionales. La recuperación de oro del 95% demuestra la eficiencia de nuestros procesos y el compromiso con la excelencia operacional.',
            'calificacion': 5,
            'proyecto_relacionado': 'Planta de Procesamiento de Minerales',
            'estado': 'activo',
            'destacado': False,
            'orden': 3
        },
        {
            'nombre': 'Roberto Vargas',
            'cargo': 'Supervisor de Seguridad',
            'empresa': 'Minera Fidami S.A.',
            'testimonio': 'La seguridad es el pilar fundamental de nuestras operaciones. Hemos implementado sistemas avanzados de monitoreo y capacitación continua. Nuestro objetivo es cero accidentes en todas las actividades mineras.',
            'calificacion': 5,
            'proyecto_relacionado': 'Sistema de Ventilación Subterránea',
            'estado': 'activo',
            'destacado': False,
            'orden': 4
        },
        {
            'nombre': 'Lucía Quispe',
            'cargo': 'Responsable de Relaciones Comunitarias',
            'empresa': 'Minera Fidami S.A.',
            'testimonio': 'Nuestro programa de desarrollo comunitario en Sancos ha generado un impacto positivo real en la comunidad. Trabajamos de manera colaborativa con las autoridades locales y la población para crear un futuro sostenible.',
            'calificacion': 5,
            'proyecto_relacionado': 'Desarrollo Comunitario Sancos',
            'estado': 'activo',
            'destacado': False,
            'orden': 5
        },
        {
            'nombre': 'Juan Pérez',
            'cargo': 'Operador de Equipos',
            'empresa': 'Minera Fidami S.A.',
            'testimonio': 'Como operador de equipos en la mina subterránea, puedo decir que Minera Fidami S.A. invierte en equipos de última generación y en la capacitación continua de su personal. Me siento orgulloso de ser parte de esta empresa.',
            'calificacion': 5,
            'proyecto_relacionado': 'Proyecto Rampa Nueva Jerusalén',
            'estado': 'activo',
            'destacado': False,
            'orden': 6
        }
    ]
    
    for testimonio_data in testimonios_data:
        Testimonio.objects.create(**testimonio_data)
    
    # 18. Certificaciones y Premios
    print("🏆 Creando certificaciones...")
    certificaciones_data = [
        {
            'nombre': 'ISO 9001:2015 - Gestión de Calidad',
            'slug': 'iso-9001-2015-gestion-calidad',
            'tipo': 'certificacion',
            'categoria': 'Gestión de Calidad',
            'descripcion': 'Certificación internacional de gestión de calidad que garantiza la excelencia en todos los procesos operativos.',
            'organismo_otorgante': 'Bureau Veritas',
            'fecha_otorgamiento': date(2022, 6, 15),
            'fecha_vencimiento': date(2025, 6, 15),
            'url_logo': 'https://example.com/iso9001-logo.png',
            'url_documento': 'https://example.com/iso9001-cert.pdf',
            'estado': 'activo',
            'orden': 1
        },
        {
            'nombre': 'ISO 14001:2015 - Gestión Ambiental',
            'slug': 'iso-14001-2015-gestion-ambiental',
            'tipo': 'certificacion',
            'categoria': 'Gestión Ambiental',
            'descripcion': 'Certificación de gestión ambiental que demuestra el compromiso con la protección del medio ambiente.',
            'organismo_otorgante': 'Bureau Veritas',
            'fecha_otorgamiento': date(2022, 8, 20),
            'fecha_vencimiento': date(2025, 8, 20),
            'url_logo': 'https://example.com/iso14001-logo.png',
            'url_documento': 'https://example.com/iso14001-cert.pdf',
            'estado': 'activo',
            'orden': 2
        },
        {
            'nombre': 'ISO 45001:2018 - Seguridad y Salud Ocupacional',
            'slug': 'iso-45001-2018-seguridad-salud-ocupacional',
            'tipo': 'certificacion',
            'categoria': 'Seguridad y Salud',
            'descripcion': 'Certificación de seguridad y salud ocupacional que garantiza condiciones de trabajo seguras.',
            'organismo_otorgante': 'Bureau Veritas',
            'fecha_otorgamiento': date(2022, 10, 10),
            'fecha_vencimiento': date(2025, 10, 10),
            'url_logo': 'https://example.com/iso45001-logo.png',
            'url_documento': 'https://example.com/iso45001-cert.pdf',
            'estado': 'activo',
            'orden': 3
        },
        {
            'nombre': 'Certificación de Seguridad Minera',
            'slug': 'certificacion-seguridad-minera',
            'tipo': 'certificacion',
            'categoria': 'Seguridad Minera',
            'descripcion': 'Certificación específica de seguridad minera otorgada por el Ministerio de Energía y Minas.',
            'organismo_otorgante': 'Ministerio de Energía y Minas',
            'fecha_otorgamiento': date(2022, 3, 15),
            'fecha_vencimiento': date(2025, 3, 15),
            'url_logo': 'https://example.com/seguridad-minera-logo.png',
            'url_documento': 'https://example.com/seguridad-minera-cert.pdf',
            'estado': 'activo',
            'orden': 4
        },
        {
            'nombre': 'Certificación Ambiental Minera',
            'slug': 'certificacion-ambiental-minera',
            'tipo': 'certificacion',
            'categoria': 'Gestión Ambiental',
            'descripcion': 'Certificación ambiental específica para operaciones mineras otorgada por el MINAM.',
            'organismo_otorgante': 'Ministerio del Ambiente',
            'fecha_otorgamiento': date(2022, 5, 20),
            'fecha_vencimiento': date(2025, 5, 20),
            'url_logo': 'https://example.com/ambiental-minera-logo.png',
            'url_documento': 'https://example.com/ambiental-minera-cert.pdf',
            'estado': 'activo',
            'orden': 5
        },
        {
            'nombre': 'Premio a la Excelencia Minera',
            'slug': 'premio-excelencia-minera',
            'tipo': 'premio',
            'categoria': 'Excelencia Operacional',
            'descripcion': 'Premio otorgado por la Sociedad Nacional de Minería, Petróleo y Energía por excelencia operacional.',
            'organismo_otorgante': 'SNMPE',
            'fecha_otorgamiento': date(2023, 11, 15),
            'fecha_vencimiento': None,
            'url_logo': 'https://example.com/excelencia-minera-logo.png',
            'url_documento': 'https://example.com/excelencia-minera-cert.pdf',
            'estado': 'activo',
            'orden': 6
        },
        {
            'nombre': 'Certificación de Responsabilidad Social',
            'slug': 'certificacion-responsabilidad-social',
            'tipo': 'certificacion',
            'categoria': 'Responsabilidad Social',
            'descripcion': 'Certificación de responsabilidad social empresarial otorgada por organización internacional.',
            'organismo_otorgante': 'SAI Global',
            'fecha_otorgamiento': date(2023, 2, 10),
            'fecha_vencimiento': date(2026, 2, 10),
            'url_logo': 'https://example.com/rs-logo.png',
            'url_documento': 'https://example.com/rs-cert.pdf',
            'estado': 'activo',
            'orden': 7
        },
        {
            'nombre': 'Certificación de Gestión de Energía ISO 50001',
            'slug': 'certificacion-gestion-energia-iso-50001',
            'tipo': 'certificacion',
            'categoria': 'Gestión Energética',
            'descripcion': 'Certificación de gestión energética que demuestra el compromiso con la eficiencia energética.',
            'organismo_otorgante': 'Bureau Veritas',
            'fecha_otorgamiento': date(2023, 6, 15),
            'fecha_vencimiento': date(2026, 6, 15),
            'url_logo': 'https://example.com/iso50001-logo.png',
            'url_documento': 'https://example.com/iso50001-cert.pdf',
            'estado': 'activo',
            'orden': 8
        }
    ]
    
    for certificacion_data in certificaciones_data:
        CertificacionPremio.objects.create(**certificacion_data)
    
    # 19. Hero Sections
    print("🎨 Creando hero sections...")
    hero_sections_data = [
        {
            'titulo_principal': 'Líderes en Minería Subterránea Sostenible',
            'subtitulo': 'Innovación, seguridad y responsabilidad social',
            'texto_boton_principal': 'Conoce Nuestros Proyectos',
            'url_boton_principal': '/proyectos/',
            'texto_boton_secundario': 'Descubre Nuestra Tecnología',
            'url_boton_secundario': '/innovacion/',
            'orden': 1,
            'activo': True
        },
        {
            'titulo_principal': 'Tecnología de Vanguardia',
            'subtitulo': 'Innovación al servicio de la minería',
            'texto_boton_principal': 'Descubre Nuestra Tecnología',
            'url_boton_principal': '/innovacion/',
            'texto_boton_secundario': 'Conoce Nuestros Proyectos',
            'url_boton_secundario': '/proyectos/',
            'orden': 2,
            'activo': True
        }
    ]
    
    for hero_data in hero_sections_data:
        HeroSection.objects.create(**hero_data)
    
    # 20. Mensajes del Sistema
    print("💬 Creando mensajes del sistema...")
    mensajes_data = [
        {
            'titulo': 'Mantenimiento Programado',
            'mensaje': 'El sitio web estará en mantenimiento el próximo domingo de 2:00 AM a 6:00 AM.',
            'tipo': 'info',
            'fecha_inicio': date(2023, 12, 20),
            'fecha_fin': date(2023, 12, 25),
            'activo': True
        }
    ]
    
    for mensaje_data in mensajes_data:
        Mensaje.objects.create(**mensaje_data)
    
    # 21. Redes Sociales
    print("📱 Creando redes sociales...")
    redes_data = [
        {
            'nombre': 'facebook',
            'url': 'https://facebook.com/minerafidami',
            'icono': 'fab fa-facebook',
            'color': '#1877F2',
            'orden': 1,
            'activo': True
        },
        {
            'nombre': 'linkedin',
            'url': 'https://linkedin.com/company/minerafidami',
            'icono': 'fab fa-linkedin',
            'color': '#0A66C2',
            'orden': 2,
            'activo': True
        },
        {
            'nombre': 'youtube',
            'url': 'https://youtube.com/minerafidami',
            'icono': 'fab fa-youtube',
            'color': '#FF0000',
            'orden': 3,
            'activo': True
        }
    ]
    
    for red_data in redes_data:
        RedSocial.objects.create(**red_data)
    
    # 22. Páginas
    print("📄 Creando páginas...")
    paginas_data = [
        {
            'titulo': 'Términos y Condiciones',
            'contenido': 'Términos y condiciones de uso del sitio web de Minera Fidami S.A.',
            'slug': 'terminos-condiciones',
            'estado': 'activo'
        },
        {
            'titulo': 'Política de Privacidad',
            'contenido': 'Política de privacidad y protección de datos personales.',
            'slug': 'politica-privacidad',
            'estado': 'activo'
        }
    ]
    
    for pagina_data in paginas_data:
        Pagina.objects.create(**pagina_data)
    
    print("✅ ¡Datos de prueba cargados exitosamente!")
    print(f"📊 Total de registros creados:")
    print(f"   - Configuración General: 1")
    print(f"   - Categorías de Servicios: {CategoriaServicio.objects.count()}")
    print(f"   - Servicios: {Servicio.objects.count()}")
    print(f"   - Categorías de Proyectos: {CategoriaProyecto.objects.count()}")
    print(f"   - Proyectos: {Proyecto.objects.count()}")
    print(f"   - Tecnologías: {Tecnologia.objects.count()}")
    print(f"   - Proyectos de Innovación: {ProyectoInnovacion.objects.count()}")
    print(f"   - Patentes: {Patente.objects.count()}")
    print(f"   - Programas Sociales: {ProgramaSocial.objects.count()}")
    print(f"   - Alianzas: {Alianza.objects.count()}")
    print(f"   - Impactos Ambientales: {ImpactoAmbiental.objects.count()}")
    print(f"   - Reportes: {ReporteSostenibilidad.objects.count()}")
    print(f"   - Categorías de Blog: {CategoriaBlog.objects.count()}")
    print(f"   - Noticias: {NoticiaBlog.objects.count()}")
    print(f"   - Vacantes: {Vacante.objects.count()}")
    print(f"   - Equipo: {Equipo.objects.count()}")
    print(f"   - Testimonios: {Testimonio.objects.count()}")
    print(f"   - Certificaciones: {CertificacionPremio.objects.count()}")
    print(f"   - Hero Sections: {HeroSection.objects.count()}")
    print(f"   - Mensajes: {Mensaje.objects.count()}")
    print(f"   - Redes Sociales: {RedSocial.objects.count()}")
    print(f"   - Páginas: {Pagina.objects.count()}")

if __name__ == '__main__':
    crear_datos_prueba() 