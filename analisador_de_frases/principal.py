"""
analisador/
├─ principal.py          * Ponto de entrada do programa (executável)
├─ analise_frase.py      * Regras principais da análise
└─ tratamento_texto.py   * Funções básicas de tratamento/preparo do texto
"""
import time
from analise_frase import analisar

PALINDROMOS_PRONTOS = [
    "A sacada da casa",
    "Socorram-me subi no onibus em Marrocos",
    "Anotaram a data da maratona"
]

def analisar_e_mostrar(frase):
    p, v, c, pal = analisar(frase)
    print("\n--- Resumo da Análise ---")
    time.sleep(0.6)
    print(f"Frase analisada: {frase}")
    time.sleep(0.6)
    print(f"Palavras: {p}")
    time.sleep(0.6)
    print(f"Vogais: {v}")
    time.sleep(0.6)
    print(f"Consoantes: {c}")
    time.sleep(0.6)
    print(f"É um palíndromo? {'Sim' if pal else 'Não'}")
    print()

def main():
    while True:
        print("=== Analisador de Frases ===")
        print("1 - Digitar minha própria frase")
        print("2 - Escolher um palíndromo pronto")
        print("3 - Encerrar programa")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            frase = input("\nDigite uma frase para analisar: ")
            analisar_e_mostrar(frase)

        elif escolha == "2":
            print("\nPalíndromos disponíveis:")
            for i, frase in enumerate(PALINDROMOS_PRONTOS, start=1):
                print(f"{i} - {frase}")
            num = input("Digite o número desejado: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(PALINDROMOS_PRONTOS):
                frase = PALINDROMOS_PRONTOS[int(num) - 1]
                analisar_e_mostrar(frase)
            else:
                print("Opção inválida!\n")

        elif escolha == "3":
            print("\nPrograma encerrado. Até mais!")
            break

        else:
            print("\nOpção inválida, tente novamente.\n")

if __name__ == "__main__":
    main()
