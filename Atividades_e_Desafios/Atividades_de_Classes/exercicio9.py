class Funcionario:
    percentual_bonus = 1.10

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        print(f"O salário de {self.nome} agora é de R$ {self.salario:.2f}")


func1 = Funcionario("Ana", 13000)
func2 = Funcionario("Breno", 25000)

print("Salário antes do bônus:")
print(f"{func1.nome}: R$ {func1.salario:.2f}")
print(f"{func2.nome}: R$ {func2.salario:.2f}")

print("\nApos aplicar o bônus...")
func1.aplicar_bonus()
func2.aplicar_bonus()
