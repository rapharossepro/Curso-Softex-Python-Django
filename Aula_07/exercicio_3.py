"""
Menu de Comandos para um Robô
- Crie um program que simula o controle de um robô simples com um menu de comandos.
1- O robô pode estar em uma posição inicial(Você pode usar uma variável para isso, por exemplo, posição 0)
2- O programa deve exibir um menu com as seguintes opções: 1- Avançar, 2- Recuar, 3- Status, 4- Desligar
3- Peça ao usuário para escolher um comando.
4- Com base na escolha, execute a ação correspondente:
    * Avançar: Adicione um valor da posição do robô
    * Recuar: Subtraia um valor da posição do robô.
    * Status: Mostre a posição atual do robô.
    * Desligar: Encerre o programa.
5- O menu deve continuar aparecendo após cada comando, até que o usuário escolha a opção "Desligar"
6- Se o usuário digitar um comando invalido, exiba uma mensagem de erro.
"""
import time

print("--- Ola, esse e o menu de controle do robo, escolha uma das opcoes a seguir: ---\n")
time.sleep(1.5)

position = 0

while True:

    print("(1) Avancar\n")
    time.sleep(0.2)
    print("(2) Voltar\n")
    time.sleep(0.2)
    print("(3) Status\n")
    time.sleep(0.2)
    print("(4) Desligar\n\b")
    time.sleep(0.2)
    

    opcao = input("")
    if opcao == "1":
        time.sleep(0.2)
        print("\nAvançando...\n")
        position += 1
        time.sleep(0.2)
    elif opcao == "2":
        time.sleep(0.2)
        print("\nRecuando...\n")
        position -= 1
        time.sleep(0.2)
    elif opcao == "3":
        print("\nLoading...\n")
        time.sleep(1.5)
        print(f"\nPosição atual: {position}\n")
    elif opcao == "4":
        print("\nDesligando o robô...")
        time.sleep(1.2)
        print("\nDesligando o robô..")
        time.sleep(1.2)
        print("\nDesligando o robô.")
        time.sleep(1.2)
        print("\nAte logo! :)\n")
        break
    else:
        time.sleep(1.2)
        print("\nOpcao invalida...\n")
        time.sleep(1.2)



