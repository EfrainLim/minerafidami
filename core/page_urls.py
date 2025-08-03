from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PaginaDetailView.as_view(), name='pagina_detail'),
] 