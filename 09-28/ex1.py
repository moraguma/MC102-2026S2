# 1 5 6 
# 1 7 9
#

def ler_linha_por_linha():
    matriz = []
    while True:
        entrada = input("Próxima linha: ")
        if entrada == "":
            return matriz

        linha = entrada.split()
        matriz.append(linha)


def imprimir_matriz(m):
    """
        Imprime uma matriz de um jeito bonito
    """
    for linha in m:
        print(linha)


imprimir_matriz(ler_linha_por_linha())
