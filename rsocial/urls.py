from django.urls import path
from . import views

app_name = 'rsocial'

urlpatterns = [
    # Página principal de responsabilidad social
    path('', views.ResponsabilidadSocialHomeView.as_view(), name='home'),
    
    # Programas sociales
    path('programas/', views.ProgramaSocialListView.as_view(), name='programa_list'),
    path('programas/<slug:slug>/', views.ProgramaSocialDetailView.as_view(), name='programa_detail'),
    
    # Alianzas
    path('alianzas/', views.AlianzaListView.as_view(), name='alianza_list'),
    path('alianzas/<slug:slug>/', views.AlianzaDetailView.as_view(), name='alianza_detail'),
    
    # Impactos ambientales
    path('impactos-ambientales/', views.ImpactoAmbientalListView.as_view(), name='impacto_list'),
    path('impactos-ambientales/<slug:slug>/', views.ImpactoAmbientalDetailView.as_view(), name='impacto_detail'),
    
    # Reportes de sostenibilidad
    path('reportes/', views.ReporteSostenibilidadListView.as_view(), name='reporte_list'),
    path('reportes/<slug:slug>/', views.ReporteSostenibilidadDetailView.as_view(), name='reporte_detail'),
    
    # Búsqueda
    path('buscar/', views.ResponsabilidadSocialSearchView.as_view(), name='search'),
] 