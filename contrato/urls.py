from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('criar/<int:id_trabalhador>', views.criar, name='criar'),
    path('listar/', views.listar, name='listar'),
    path('detail/<int:id>', views.detail, name='detail'), 
    path('editar/<int:id>', views.editar, name='editar'), 
    path('cancelar/<int:id>', views.cancelar, name='cancelar'),
    path('finalizar/<int:id>', views.finalizar, name='finalizar')
]