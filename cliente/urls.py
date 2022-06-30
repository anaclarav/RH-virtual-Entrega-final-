from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('criar/', views.criar, name='criar'),
    #path('listar/', views.listar, name='listar'),
    path('detail/<int:id>', views.detail, name='detail'), 
    path('editar/<int:id>', views.editar, name='editar'), 
    path('meu-perfil/<int:id>', views.meuperfil, name='meuperfil')
    #path('deletar/<int:id>', views.deletar, name='deletar')
]