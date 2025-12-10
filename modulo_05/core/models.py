from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):


    # Opções de escolha para o campo prioridade
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    # --- Relacionamentos ---
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tarefas',
        verbose_name='Usuário'
    )

    # --- Campos de Dados ---
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título' # Substitui o antigo 'nome' para manter padrão do trecho mais completo
    )

    descricao = models.TextField(
        blank=True, 
        null=True,
        verbose_name='Descrição'
    )

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
        verbose_name='Prioridade'
    )

    prazo = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Prazo de Entrega'
    )

    # --- Campos de Status e Controle ---
    concluida = models.BooleanField(
        default=False,
        verbose_name='Concluída'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em'
    )

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']  # Ordena das mais recentes para as mais antigas

    def __str__(self):
        """Representação em string do objeto"""
        status = '✓' if self.concluida else '✗'
        return f"{self.titulo} ({status}) - {self.get_prioridade_display()}"