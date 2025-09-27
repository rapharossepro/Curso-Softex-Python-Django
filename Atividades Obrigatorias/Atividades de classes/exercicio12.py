class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"


meu_filme = Filme("Shooter – O Atirador", "Antoine Fuqua", 2007)
print(meu_filme)
