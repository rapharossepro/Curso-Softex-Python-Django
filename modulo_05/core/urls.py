from django.urls import path
from .views import ListaTarefasAPIView, EstatisticasTarefasAPIView

# Namespace do app (facilita referenciar URLs no código com 'core:nome-da-url')
app_name = 'core'

urlpatterns = [
    # Endpoint para listar e criar tarefas
    # URL Final: /api/tarefas/
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),

    # Endpoint para ver estatísticas (total, pendentes, taxa de conclusão)
    # URL Final: /api/tarefas/estatisticas/
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
]