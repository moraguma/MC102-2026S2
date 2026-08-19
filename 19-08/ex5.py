dia_1 = int(input("Dia da primeira data"))
mes_1 = int(input("Mês da primeira data"))
ano_1 = int(input("Ano da primeira data"))

dia_2 = int(input("Dia da segunda data"))
mes_2 = int(input("Mês da segunda data"))
ano_2 = int(input("Ano da segunda data"))

if ano_1 > ano_2:
    print("Primeira data vem depois")
elif ano_1 < ano_2:
    print("Segunda data vem depois")
elif mes_1 > mes_2:
    print("Primeira data vem depois")
elif mes_1 < mes_2:
    print("Segunda data vem depois")
elif dia_1 > dia_2:
    print("Primeira data vem depois")
elif dia_1 < dia_2:
    print("Segunda data vem depois")
else:
    print("Mesma data!")