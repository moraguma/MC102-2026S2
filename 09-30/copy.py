a = [
    [1, 2, 3],
    [4, 5, 6]
]
b = a.copy()

b[1][1] = 7
print(a)
print(b)