"""
Simulação de Pedido em uma lanchonete
- Crie um programa que simula um sistema de pedido em uma lanchonete.
1- Defina o preço de um hambúrger.
2- Defina um código de cupom de desconto.
3- O programa deve pedir ao cliente o nom e do produto repetidamente até que o produto correto seja digitado.
4- Após a escolha, o programa deve perguntar se o cliente tem um cupom de desconto.
5- Se o cliente digitar um  cupom corretamente, aplique o desconto.
6- Calcule o preço final e exiba o total a pagar.
7- O programa deve encerrrar após o pedido ser finalizado.
"""

valor_hamburger = 20.00
cupom_desconto = "12345"

print("Bem vindo ao MegaBurger SA, confira nosso cardapio e faca seu pedido.\n")

while True:
   lanche = input("Qual hamburger voce deseja?\n")
   if lanche == "hamburger":
      print("Pedido recebido.")
      break
   else:
      print("Este lanche não esta no cardapio, tente novamente.\n")

cupom = input("Digite seu cupom de desconto: \n")
if cupom == cupom_desconto:
   print(f"Seu lanche custou {valor_hamburger * 0.9}\n")
else:
   print(f"Seu lanche custou {valor_hamburger}\n ")