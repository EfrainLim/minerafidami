from django.urls import path
from . import views

app_name = 'servicios'

urlpatterns = [
    path('', views.ServicioListView.as_view(), name='servicio_list'),
    path('<slug:slug>/', views.ServicioDetailView.as_view(), name='servicio_detail'),
    path('categoria/<slug:slug>/', views.CategoriaServicioView.as_view(), name='categoria_servicio'),
] 