from django.urls import path
from . import views

urlpatterns = [
    # Pagina Inicial
    path('', views.index, name='index'),
    
    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
    
    # Mostra o Tópico necessário
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Pagina para adicionar um novo assunto
    path('topics/new_topic/', views.new_topic, name='new_topic'),
    
    # Visualization of Url
    path('url/', views.url, name='url'),
    
    # Url Form
    path('url_form/', views.new_url, name='new_url'),
]
