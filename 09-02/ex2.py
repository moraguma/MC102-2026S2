n = int(input("n = "))

minha_lista = []
for i in range(n):
    minha_lista.append(int(input("Número: ")))

resultado = True
for i in range(1, n):
    if minha_lista[i - 1] > minha_lista[i]:
        resultado = False
        break

if resultado:
    print("Crescente")
else:
    print("Não crescente")