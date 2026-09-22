def levar_dano(vida, dano):
    if dano >= 0:
        vida -= dano

    if vida < 0:
        vida = 0

    print(vida)
    return vida


vida = 20

vida = levar_dano(vida, 5)
vida = levar_dano(vida, 5)
        