a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a > b and a > c:
    print(a, "é o maior número")
elif b > a and b > c:
    print(b, "é o maior número")
else:
    print(c, "é o maior número")