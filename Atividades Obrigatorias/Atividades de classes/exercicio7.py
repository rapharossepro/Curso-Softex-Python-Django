class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


retangulo1 = Retangulo(5, 3)
retangulo2 = Retangulo(10, 2)
retangulo3 = Retangulo(4, 4)
retangulo4 = Retangulo(8, 6)
retangulo5 = Retangulo(7, 5)

lista_retangulos = [retangulo1, retangulo2, retangulo3, retangulo4, retangulo5]

for i, ret in enumerate(lista_retangulos, start=1):
    print(f"Retângulo {i}:")
    print(f"  Base: {ret.base}")
    print(f"  Altura: {ret.altura}")
    print(f"  Área: {ret.calcular_area()}")
    print(f"  Perímetro: {ret.calcular_perimetro()}")
    print("<->" * 10)
