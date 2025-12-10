from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    # Redefinimos o campo explicitamente apenas para adicionar as mensagens de erro personalizadas
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode estar vazio.',
            'max_length': 'O título não pode exceder 200 caracteres.'
        }
    )

    class Meta:
        model = Tarefa
        # Lista completa unindo os campos do primeiro e segundo exemplo
        fields = [
            'id', 
            'user', 
            'titulo', 
            'descricao', 
            'prioridade', 
            'prazo', 
            'concluida', 
            'criada_em'
        ]
        # Campos que o frontend recebe, mas não pode alterar/criar manualmente
        read_only_fields = ['id', 'criada_em', 'user']

    def validate_titulo(self, value):
        """
        Validação customizada para o campo 'titulo'.
        Regras:
        - Não pode ser vazio (após strip)
        - Não pode conter apenas números
        - Deve ter pelo menos 3 caracteres
        """
        # Remover espaços em branco extras
        value = value.strip()

        # Validação 1: Não vazio
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )

        # Validação 2: Mínimo de caracteres
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )

        # Validação 3: Não apenas números
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )

        return value