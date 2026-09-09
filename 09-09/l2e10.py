numero = int(input("Número a converter: "))

base = 1
while base <= numero:
    base *= 2

resultado = []
while numero != 0 or base != 1:
    base /= 2
    if numero - base >= 0:
        resultado.append("1")
        numero -= base
    else:
        resultado.append("0")

print("".join(resultado))