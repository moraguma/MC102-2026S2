n = int(input("Quantos números serão lidos? "))

numeros = []
for i in range(n):
    numeros.append(int(input("Novo número: ")))

numeros = [int(input("Novo número: ")) for i in range(n)]
print(numeros)
