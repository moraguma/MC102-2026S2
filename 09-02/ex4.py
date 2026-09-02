m = int(input("m = "))
seq_m = []
for i in range(m):
    seq_m.append(input("Caractere: "))
print(seq_m)

n = int(input("n = "))
seq_n = []
for i in range(n):
    seq_n.append(input("Caractere: "))

print(seq_n)

posicoes = []
for i in range(0, m - n + 1):
    if seq_m[i:i + n] == seq_n:
        posicoes.append(i)
        print("Achei")

print(posicoes)