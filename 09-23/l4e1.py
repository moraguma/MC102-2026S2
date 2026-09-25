def inverte(palavra):
    """
        Retorna a palavra invertida
    """
    resultado = ""
    for i in range(len(palavra) - 1, -1, -1):
        resultado += palavra[i]

    return resultado

print(inverte("Arroz"))
print(inverte("Zorra"))
