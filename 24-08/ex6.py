n = int(input("n = "))
resultado = ""

i = 2
while n != 1:
    while n % i == 0:
        n /= i
        print(i)
    i += 1