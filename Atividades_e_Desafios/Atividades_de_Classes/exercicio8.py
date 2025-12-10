import time

class Carro:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.marcador_combustivel = 0

    def abastecer(self, litros):
        self.marcador_combustivel += litros
        print(f"{litros} litro(s) abastecido(s). Combustível atual: {self.marcador_combustivel} L.")
        time.sleep(1.5)

    def dirigir(self, distancia):
        combustivel_necessario = distancia / 18
        if combustivel_necessario <= self.marcador_combustivel:
            self.marcador_combustivel -= combustivel_necessario
            print(f"O carro {self.modelo} percorreu {distancia} km.")
            time.sleep(1.5)
            print(f"Combustível restante: {self.marcador_combustivel:.1f} L.")
            time.sleep(1.5)
        else:
            print(f"Combustível insuficiente para {distancia} km!")
            time.sleep(1.5)
            print(f"Combustível disponível: {self.marcador_combustivel:.1f} L.")
            time.sleep(1.5)



carro1 = Carro("Uno 1.0")

carro1.dirigir(30)
carro1.abastecer(20)
carro1.dirigir(30)
carro1.dirigir(25)
carro1.dirigir(100)
