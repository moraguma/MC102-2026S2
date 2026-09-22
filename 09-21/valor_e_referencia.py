def por_valor(x):
    x = 6
    pass

def por_referencia(l):
    l.append("B")
    pass

x = 3
por_valor(x)
print(x)

l = ["A"]
por_referencia(l)
print(l)