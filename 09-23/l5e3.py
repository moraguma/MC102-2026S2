def satisfaz(n, b, k):
    return b ** k == n


def menor_base_log(n):
    if n == 1:
        return 1

    for b in range(2, n + 1):
        k = 0
        while True:
            if satisfaz(n, b, k): 
                return b
            
            k += 1
            if b ** k > n:
                break

print(menor_base_log(1))
print(menor_base_log(27))
print(menor_base_log(12))
print(menor_base_log(144000))