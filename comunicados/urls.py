from django.urls import path
from . import views

app_name = 'comunicados'

urlpatterns = [
    path('', views.ComunicadoListView.as_view(), name='comunicado_list'),
    path('<slug:slug>/', views.ComunicadoDetailView.as_view(), name='comunicado_detail'),
] 