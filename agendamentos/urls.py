from agendamentos import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendar/', views.agendar, name='agendar'),
    path('agendamentos/', views.ver_agendamentos, name='ver_agendamentos'),
    path('editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('fatura/<int:pk>/', views.gerar_fatura_pdf, name='gerar_fatura_pdf'),
]
