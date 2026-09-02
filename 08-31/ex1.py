n = int(input("n = "))

a_somar = list(range(1, n + 1))

resultado = 0
for elemento in a_somar:
    resultado += elemento

print(resultado)