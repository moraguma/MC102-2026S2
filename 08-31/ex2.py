n = int(input("n = "))
m = int(input("m = "))
y = int(input("y = "))
x = int(input("x = "))

for i in range(n):
    linha = ""
    for j in range(m):
        if i == y and j == x:
            linha += "1"
        else:
            linha += "0"
    print(linha)