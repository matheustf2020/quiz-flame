from django.urls import path
from . import views

urlpatterns = [
    path('bem_vindo/', views.bem_vindo, name='bem_vindo'),
    path('<int:numero>/', views.pergunta_view, name='pergunta'),
    path('resultado/', views.resultado_view, name='resultado'),
    path('nome/', views.nome_view, name='nome'),    

]
