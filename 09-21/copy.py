def print_menor(l):
    l.sort()
    print(l[0])


l = [2, 5, 7, 1, -3, 4, 7]
print_menor(l.copy())
print(l)