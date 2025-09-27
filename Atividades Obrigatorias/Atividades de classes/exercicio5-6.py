import time

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")
            print(f"Saldo atual permanece: R$ {self.saldo:.2f}")

time.sleep(1)
conta1 = ContaBancaria("Rapha", 16100.00)
time.sleep(2)
conta1.depositar(1050.00)
time.sleep(2)
conta1.sacar(800.00)
time.sleep(2)
conta1.sacar(2200.00)
