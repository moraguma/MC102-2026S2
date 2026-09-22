def checa_idade(idade):
    if idade <= 3:
        return "Bebê"
    elif idade <= 6:
        return "Criança"
    elif idade <= 12:
        return "Pré adolescente"
    elif idade <= 17:
        return "Adolescente"
    else:
        return "Adulto"

print(checa_idade(13))
print(checa_idade(27))
print(checa_idade(2))
