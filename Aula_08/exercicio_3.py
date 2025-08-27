"""
Crie um programa que codifica e decodifica uma frase, seguindo as regras abaixo:
1- Cada vogal deve ser substituida pelo número correspondente:
    a => 1
    e => 2
    i => 3
    o => 4
    u => 5

2- O programa deve:
    * Ler uma frase digitada pelo usuário.
    * Exibir a frase codificada, trocando as vogais pelos números.
    * Exibir a frase decodificada, voltando os números às vogais originais.

"""
frase_original = input("Digite uma frase: ").lower()
frase_codificada = frase_original.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
frase_decodificada = frase_original.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")

print(frase_codificada)
print(frase_decodificada)


        


