def palindromo(palavra, inicio, final):
    if final - inicio <= 1:
        return True

    if palavra[inicio] == palavra[final] and palindromo(palavra, inicio + 1, final - 1):
        return True
    return False


print(palindromo("ameopoema", 0, 8))