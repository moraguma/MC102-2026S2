def ler_notas():
    notas = []
    while True:
        entrada = input()
        if entrada == "":
            return notas

        notas.append([float(x) for x in entrada.split()])


def passaram(alunos):
    aprovados = []
    for i in range(len(alunos)):
        media = (alunos[i][0] + alunos[i][1] * 2 + alunos[i][2] * 3) / 6.0
        if media >= 5:
            aprovados.append(i)

    return aprovados


def maiores_notas(alunos):
    maior_nota = 0.0
    melhores_alunos = []
    for i in range(len(alunos)):
        media = (alunos[i][0] + alunos[i][1] * 2 + alunos[i][2] * 3) / 6.0
        if media == maior_nota:
            melhores_alunos.append(i)
        elif media > maior_nota:
            maior_nota = media
            melhores_alunos = [i]

    return melhores_alunos


alunos = [
    [4.6, 2.9, 10.0],
    [3.4, 2.1, 5.1],
    [10.0, 10.0, 7.0],
    [54.0, 0.0, 0.0],
    [7.0, 10.0, 9.0]
]
print(maiores_notas(alunos))