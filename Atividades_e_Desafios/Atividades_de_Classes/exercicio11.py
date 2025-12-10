class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def listar_livros(self):
        print("Nosso acervo e composto por:")
        for livro in self.acervo:
            print("__" * 30)
            print(f"-> {livro.titulo} (Autor: {livro.autor})")
            print("__" * 30)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(Livro("O Investidor Inteligente", "Benjamin Graham"))
biblioteca.adicionar_livro(Livro("Pai Rico, Pai Pobre", "Robert T. Kiyosaki"))
biblioteca.adicionar_livro(Livro("Um Passeio Aleatório pela Bolsa de Valores", "Burton G. Malkiel"))

biblioteca.adicionar_livro(Livro("A Interpretação dos Sonhos", "Sigmund Freud"))
biblioteca.adicionar_livro(Livro("O Eu e o Id", "Sigmund Freud"))
biblioteca.adicionar_livro(Livro("O Seminário, Livro 11: Os Quatro Conceitos Fundamentais da Psicanálise", "Jacques Lacan"))
biblioteca.adicionar_livro(Livro("O Brincar e a Realidade", "Donald W. Winnicott"))

biblioteca.listar_livros()
