import random

def escolher(lista_01:list[int], lista_02:list[int]) -> list[int]:
    conjunto_01 = set(lista_01)
    conjunto_02 = set(lista_02)
    resultado = conjunto_01.intersection(conjunto_02)
    return list(resultado)