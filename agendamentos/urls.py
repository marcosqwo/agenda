from django.urls import path

from agendamentos.views import AgendamentosView, AgendamentoAddView, AgendamentoUpdateView, AgendamentoDeleteView, \
    AgendamentoInLineEditView, AgendamentoExibir, AgendamentoGraficoView

urlpatterns = [
    path('agendamentos',AgendamentosView.as_view(), name='agendamentos'),
    path('agendamento/adicionar',AgendamentoAddView.as_view(), name='agendamento_adicionar'),
    path('<int:pk>/agendamento/editar',AgendamentoUpdateView.as_view(), name='agendamento_editar'),
    path('<int:pk>/agendamento/apagar',AgendamentoDeleteView.as_view(), name='agendamento_apagar'),
    path('<int:pk>/agendamento/inline',AgendamentoInLineEditView.as_view(), name='agendamento_inline'),
    path('<int:pk>/agendamento/exibir',AgendamentoExibir.as_view(), name='agendamento_exibir'),
    path('agendamentos/grafico',AgendamentoGraficoView.as_view(), name='agendamentos_grafico'),

]