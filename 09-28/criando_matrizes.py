# M - largura
# N - altura

m = int(input("M = "))
n = int(input("N = "))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(input(f"Insira item na posição {(i, j)}"))
    matriz.append(linha)

print(matriz)
    
    