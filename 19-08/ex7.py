# ax² + bx + c = 0
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        print(c, "= 0", c == 0.0)
    else:
        x = -c / b
        print("x =", x)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Sem soluções reais")
    else:
        x_1 = (-b + delta ** 0.5) / (2 * a)
        x_2 = (-b - delta ** 0.5) / (2 * a)

        print("x1 =", x_1, "; x2 =", x_2)