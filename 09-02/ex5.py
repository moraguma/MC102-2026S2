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

intersecao = []
for i in range(n):
    for j in range(m):
        if seq_n[i] == seq_m[j]:
            intersecao.append(seq_n[i])

print(intersecao)