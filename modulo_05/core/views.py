import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Tarefa
from .serializers import TarefaSerializer

# Configuração do Logger
logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    """
    View para listar tarefas e criar novas tarefas.
    """
    
    def get(self, request):
        logger.info("Acessando lista de tarefas")
        
        # Filtra por user_id se passado na URL, senão traz tudo (ou poderia filtrar pelo user logado)
        user_id = request.query_params.get('user_id')
        
        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            # DICA: Em produção, idealmente filtrar por request.user para segurança
            tarefas = Tarefa.objects.all()
        
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            
            if serializer.is_valid():
                # O campo 'user' é read_only no serializer, então precisamos
                # injetar o usuário logado (request.user) manualmente ao salvar.
                # Certifique-se de que o usuário esteja autenticado.
                if request.user.is_authenticated:
                    serializer.save(user=request.user)
                else:
                    return Response(
                        {"error": "Usuário precisa estar logado para criar tarefas."}, 
                        status=status.HTTP_401_UNAUTHORIZED
                    )

                logger.info(f"Tarefa criada com sucesso: ID {serializer.data.get('id')}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            
            # Se o serializer não for válido
            logger.warning(f"Falha na validação dos dados: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except IntegrityError as e:
            # Erro de integridade do banco (ex: dados duplicados ou chaves inválidas)
            logger.error(f"Erro de integridade ao criar tarefa: {str(e)}")
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except Exception as e:
            # Erro genérico inesperado
            logger.critical(f"Erro interno no servidor: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class EstatisticasTarefasAPIView(APIView):
    """
    Retorna estatísticas gerais sobre as tarefas.
    Unifica a contagem simples e o cálculo de taxa de conclusão.
    """
    def get(self, request):
        total = Tarefa.objects.count()
        # Ajustado para usar 'concluida=True' (Boolean) conforme o models.py
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        
        # Cálculo seguro da taxa (evita divisão por zero)
        taxa_conclusao = (concluidas / total * 100) if total > 0 else 0
        
        return Response({
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao_percentual": round(taxa_conclusao, 2)
        }, status=status.HTTP_200_OK)