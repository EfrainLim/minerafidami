from django.urls import path
from . import views

app_name = 'proyectos'

urlpatterns = [
    path('', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('<slug:slug>/', views.ProyectoDetailView.as_view(), name='proyecto_detail'),
    path('categoria/<slug:slug>/', views.CategoriaProyectoView.as_view(), name='categoria_proyecto'),
] 