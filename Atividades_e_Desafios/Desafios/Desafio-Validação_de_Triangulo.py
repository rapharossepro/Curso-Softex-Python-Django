"""
Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.
"""

import time

while True:
    print("\nDigite os valores dos lados do triângulo:")
    time.sleep(1)

    lA = input("Lado A: ")
    lB = input("Lado B: ")
    lC = input("Lado C: ")

    print("\nValidando os valores...")
    time.sleep(1.5)

    if lA.isdigit() and lB.isdigit() and lC.isdigit():
        lA = int(lA)
        lB = int(lB)
        lC = int(lC)

        print("Checando se são positivos...")
        time.sleep(1.5)

        if lA > 0 and lB > 0 and lC > 0:

            print("Aplicando as regras do triângulo...")
            time.sleep(2)

            cond_soma = (lA < lB + lC) and (lB < lA + lC) and (lC < lA + lB)

            cond_dif = (lA > abs(lB - lC)) and (lB > abs(lA - lC)) and (lC > abs(lA - lB))

            if cond_soma and cond_dif:
                print("\nOs valores podem formar um triângulo!")
                time.sleep(1)
                print("Finalizando aplicação.")
                break
            else:
                print("\nEsses valores NÃO podem formar um triângulo.")
                time.sleep(1)
                print("Tente novamente...")
                time.sleep(1.5)
        else:
            print("\nErro: os valores devem ser positivos.")
            time.sleep(1)
    else:
        print("\nErro: você deve digitar apenas números inteiros.")
        time.sleep(1)
