class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Caderno", 15.50)
produto2 = Produto("Caneta", 3.00)

print(f"Produto: {produto1.nome}, Preço: R$ {produto1.preco}")
print(f"Produto: {produto2.nome}, Preço: R$ {produto2.preco}")