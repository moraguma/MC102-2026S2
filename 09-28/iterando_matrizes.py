matriz = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{(j, i)} - {matriz[j][i]}")