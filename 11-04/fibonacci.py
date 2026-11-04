def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_mem(n, mem):
    """
        mem[n] = fibonacci_mem(n)
    """
    if n == 0 or n == 1:
        return 1

    if not n - 1 in mem:
        mem[n - 1] = fibonacci_mem(n - 1, mem)
    if not n - 2 in mem:
        mem[n - 2] = fibonacci_mem(n - 2, mem)

    return mem[n - 1] + mem[n - 2]
    


print(fibonacci_mem(4, {}))