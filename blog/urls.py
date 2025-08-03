from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('categoria/<slug:slug>/', views.CategoriaBlogView.as_view(), name='categoria_blog'),
] 