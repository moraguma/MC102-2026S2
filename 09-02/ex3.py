n = int(input("n = "))

numeros = []
for i in range(n):
    numeros.append(int(input("Numero = ")))

media = 0
for numero in numeros:
    media += numero
media /= n

somatorio = 0
for i in range(n):
    somatorio += (numeros[i] - media) ** 2
somatorio /= (n - 1)

print(somatorio ** 0.5)
