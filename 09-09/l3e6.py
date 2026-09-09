l1 = input("L1: ").split()
for i in range(len(l1)):
    l1[i] = int(l1[i])

l2 = input("L2: ").split()
for i in range(len(l2)):
    l2[i] = int(l2[i])

resultado = []
i = 0
j = 0
while i + j < len(l1) + len(l2):
    if i >= len(l1):
        resultado.append(l2[j])
        j += 1
        continue
    elif j >= len(l2):
        resultado.append(l1[i])
        i += 1
        continue

    if l1[i] < l2[j]:
        resultado.append(l1[i])
        i += 1
    else:
        resultado.append(l2[j])
        j += 1
print(resultado)