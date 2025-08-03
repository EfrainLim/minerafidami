from django.urls import path
from . import views

app_name = 'carreras'

urlpatterns = [
    path('', views.VacanteListView.as_view(), name='vacante_list'),
    path('<slug:slug>/', views.VacanteDetailView.as_view(), name='vacante_detail'),
    path('<slug:slug>/postular/', views.postular_vacante, name='postular_vacante'),
] 