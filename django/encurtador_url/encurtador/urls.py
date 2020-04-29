from django.urls import path
from . import views

urlpatterns = [
    # Pagina Inicial
    path('', views.new_link, name='new_link'),

    # Link encurtado
    path('<int:link_id>/', views.link, name='link'),

    # Rank
    path('rank/', views.rank, name='rank'),
]