numeros = [0, 1, 20, 3, -2, 14, 7, 31]

numeros_grandes = []
for numero in numeros:
    if numero > 10:
        numeros_grandes.append(numero)

numeros_grandes = [numero for numero in numeros if numero > 10]

print(numeros_grandes)