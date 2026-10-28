def contagem_vogais(palavra, n):
    if n == 0:
        return 0

    tem_vogal = 0
    if palavra[n - 1] in "aeiou":
        tem_vogal = 1
    
    return contagem_vogais(palavra, n - 1) + tem_vogal


print(contagem_vogais("maca", 4))