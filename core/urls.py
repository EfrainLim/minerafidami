from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sobre-nosotros/', views.SobreNosotrosView.as_view(), name='sobre_nosotros'),
    path('equipo/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipo/<slug:slug>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
] 