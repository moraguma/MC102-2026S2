def eh_trio_pitagorico(a, b, n):
    return a ** 2 + b ** 2 == n


def eh_pitagorico(n):
    a = 1
    while a ** 2  < n:
        b = a
        while a ** 2 + b ** 2 <= n:
            if eh_trio_pitagorico(a, b, n):
                return True
            b += 1
        a += 1

    return False


print(eh_pitagorico(6))