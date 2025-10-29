"""
Validação e Formatação de Telefone
- Crie um programa que recebe um número de telefone com 11 dígitos.

1- O número é considerado *INVÁLIDO* se tiver 3 ou mais digitos iguais.
2- O programa deve verificar se o número tem 11 dígitos e se todos os caracteres são números.
3- Se o número for válido, o programa deve formatá-lo para o padrão (xx) xxxxx-xxxx.
4- O programa deve imprimir o número formatado ou a mensagem de erro correspondente.
"""

telefone = input("Digite o número do telefone para verificar se ele é válido: ")

check = 0

if len(telefone) != 11:
    print("Tamanho incorreto!")
elif not telefone.isdigit():
    print("Telefone inválido!")
else:
    valido = True
    for c in telefone:
        cont = 0
        for d in telefone:
            if d == c:
                cont += 1
        if cont >= 3:
            valido = False
            break
    
    if not valido:
        print("Não é possivel gerar um número de telefone com esse valor!")
    else:
        print("("+telefone[0]+telefone[1]+") "+telefone[2]+telefone[3]+telefone[4]+telefone[5]+telefone[6]+"-"+telefone[7]+telefone[8]+telefone[9]+telefone[10])