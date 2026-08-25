n = int(input("n = "))

c = 1
while c <= n:
    b = 1
    while b <= c:
        a = 1
        while a <= b:
            if a**2 + b**2 == c**2:
                print(a, "² +", b, "² =", c, "²")
            a += 1

        b += 1

    c += 1