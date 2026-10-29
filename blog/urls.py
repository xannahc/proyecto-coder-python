from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='inicio'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detalle_post'),
    path('posts/crear/', views.PostCreateView.as_view(), name='crear_post'),
    path('posts/<int:pk>/editar/', views.PostUpdateView.as_view(), name='editar_post'),
    path('posts/<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='eliminar_post'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
]
