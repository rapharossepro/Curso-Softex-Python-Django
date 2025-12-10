class Motor:
    def __init__(self, potencial):
        self.potencial = potencial

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem motor de {self.motor.potencial} cv de potência.")


gurgel = Carro("Gurgel BR-800 Supermini", 36)
opala = Carro("Opala V8 Turbo", 450)

gurgel.exibir_potencia()
opala.exibir_potencia()
