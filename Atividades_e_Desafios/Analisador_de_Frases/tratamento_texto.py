def contar_palavras(texto):
    partes = texto.split()
    return len(partes)

def filtrar_letras(texto):
    letras = []
    for ch in texto:
        if ch.isalpha():
            letras.append(ch)
    return letras