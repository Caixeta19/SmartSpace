from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_salas, name='listar_salas'),
    path('salas/', views.listar_salas, name='listar_salas'),
    path('sala/<int:id>/', views.agendar_sala, name='agendar_sala'),
    path('agendar/', views.agendar_sala, name='agendar_sala'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('meusagendamentos/', views.listar_meus_agendamentos, name='listar_meus_agendamentos'),
    path('agendamento/editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamento/excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('gerenciarsala/', views.gerenciar_sala, name='gerenciar_salas'),
    path('exportarrelatorio/<str:relatorio>/', views.exportar_relatorio, name='exportar_relatorio'),
     path('agendamentoscancelados/<int:pk>/', views.confirmar_cancelamento, name='confirmar_cancelamento'),
     path('agendamentoscancelados/', views.listar_cancelamentos, name='agendamentos_cancelados'),

]



