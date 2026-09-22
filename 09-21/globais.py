mensagem = "Olá"

def minha_funcao():
    global mensagem # Explicitando que é a global
    mensagem += "\nTchau"
    print(mensagem)

minha_funcao()
minha_funcao()
print(mensagem)