from django.urls import path
from . import views

app_name = 'storeapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamentos, name='departamentos'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:id>/', views.categorias, name='categorias_por_id'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/<int:id>/', views.produtos, name='produtos_por_id'),
    path('produto_detalhes/', views.produto_detalhes, name='produto_detalhes'),
    path('produto_detalhes/<int:id>/', views.produto_detalhes, name='produto_detalhes_por_id'),
    path('institucional/', views.institucional, name='institucional'),
    path('contato/', views.contato, name='contato'),
    path('contato/enviar/', views.enviar_email, name='enviar_contato')
]
