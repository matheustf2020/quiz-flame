from django.urls import path
from . import views

urlpatterns = [
    path('bem_vindo/', views.bem_vindo, name='bem_vindo'),
    path('<int:numero>/', views.pergunta_view, name='pergunta'),
    path('resultado/', views.resultado_view, name='resultado'),
    #path('nome/', views.nome_view, name='nome'),
    path('resetar_perguntas/', views.resetar_perguntas, name='resetar_perguntas'),
    path('manutencao/', views.manutencao, name='manutencao'),
    path('logar/', views.logar, name='logar'),
    path('painel/', views.painel_usuario, name='painel'),
    path('sair/', views.sair, name='sair'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),

]
