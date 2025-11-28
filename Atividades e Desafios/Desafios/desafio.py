"""
Comércio Padaria - Desafio Python
x 1- O programa tem que rodar em loop infinito até ser parado pelo usuário.
x 2- Cliente pedir um tipo de pão (Frances, Doce, Forma, Australiano) 
x 3- Cada pão terá uma quantidade 
x 4- Valor do produto 
x 5- Pedir formas de pagamento (Dinheiro, Cartão, Pix)
x 6- Forma de entrega
x 7- Dados do Cliente (Em caso de delivery)
x 8- Valor do frete por bairro 
x 9- Nome do atendente 
x 10- Codigo de entrega
"""
## Nomes dos pães
nome_frances = "FRANCES"
nome_doce = "DOCE"
nome_forma = "FORMA"

## Valor dos pães
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99

## Quantidade dos pães
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

## Nome do atendente
nome_atendente = "Maria"

## Nome dos bairros
bairro_barroco = "Barroco"
bairro_sao_jose = "São José"

## Frete pros bairros
frete_barroco = 5.00
frete_sao_jose = 15.00

# Codigo de venda
codigo_venda = 9856

while True:
    print(f"-- Bem vindo a padaria Desespero, sou a atendente {nome_atendente}")
    escolha = input(f"Temos pão: {nome_frances}, {nome_doce}, {nome_forma}. Qual pão você deseja? ").upper()
    if escolha == nome_frances:
        quantidade = int(input("Qual a quantidade: "))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f"O valor do pedido é R$ {valor_compra}.")
        else:
            print(f"Infelizmente só temos {quantidade_frances} no momento!")
            break

    forma_entrega = input("Digite 1 para retirar e 2 para entregar?")
    if forma_entrega == "2":
        bairro_entrega = input(f"Digite 1: {bairro_barroco} e 2: {bairro_sao_jose}")
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f"Valor do frete R$ {valor_frete}")
        elif bairro_entrega == "2":
            valor_frete = frete_sao_jose
            print(f"Valor do frete R$ {valor_frete}")
        else:
            print("Fora da área de entrega")
            break
    elif forma_entrega == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input("Informe seu nome: ")
    forma_pagamento = input(f"Qual forma de pagamento: 1-dinheiro ou 2-cartão")
    if forma_pagamento == "1":
        forma_pagamento = "Dinheiro"
    else:
        forma_pagamento = "Cartão"

codigo_atual = codigo_venda + 1
print(f"O valor total da sua compra foi de R$ {valor_compra + valor_frete}")