from django.urls import path
from . import views

app_name = 'innovacion'

urlpatterns = [
    # Página principal de innovación
    path('', views.InnovacionHomeView.as_view(), name='home'),
    
    # Tecnologías
    path('tecnologias/', views.TecnologiaListView.as_view(), name='tecnologia_list'),
    path('tecnologias/<slug:slug>/', views.TecnologiaDetailView.as_view(), name='tecnologia_detail'),
    
    # Proyectos de innovación
    path('proyectos/', views.ProyectoInnovacionListView.as_view(), name='proyecto_list'),
    path('proyectos/<slug:slug>/', views.ProyectoInnovacionDetailView.as_view(), name='proyecto_detail'),
    
    # Patentes
    path('patentes/', views.PatenteListView.as_view(), name='patente_list'),
    path('patentes/<slug:slug>/', views.PatenteDetailView.as_view(), name='patente_detail'),
    
    # Búsqueda
    path('buscar/', views.InnovacionSearchView.as_view(), name='search'),
] 