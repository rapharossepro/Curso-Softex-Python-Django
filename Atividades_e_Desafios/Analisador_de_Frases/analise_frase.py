from tratamento_texto import contar_palavras, filtrar_letras

def contar_vogais_consoantes(texto):
    vogais = "aeiouAEIOU"
    letras = filtrar_letras(texto)
    total_vogais = 0
    for ch in letras:
        if ch in vogais:
            total_vogais += 1
    total_consoantes = len(letras) - total_vogais
    return total_vogais, total_consoantes

def verificar_palindromo(texto):
    filtrado = ""
    for ch in filtrar_letras(texto):
        letra = ch.lower()
        filtrado += letra

    invertido = ""
    for i in range(len(filtrado) - 1, -1, -1):
        invertido += filtrado[i]

    if filtrado == invertido:
        return True
    else:
        return False

def analisar(texto):
    p = contar_palavras(texto)
    v, c = contar_vogais_consoantes(texto)
    pal = verificar_palindromo(texto)
    return p, v, c, pal

def analisar_frase(texto):
    return analisar(texto)