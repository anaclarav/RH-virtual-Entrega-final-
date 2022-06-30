from django.urls import include, path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro.as_view(), name='cadastro'),
    path('login/',include('django.contrib.auth.urls')),
    path('escolha/', views.tipoUsuario, name='tipoUsuario')
]
