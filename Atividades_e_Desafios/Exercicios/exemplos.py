numeros = [10, 15, 22, 33, 40, 45, 55, 60, 2, 7]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("\nNúmeros ímpares:", impares)