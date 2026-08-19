jogada_1 = input("Jogada 1: ")
jogada_2 = input("Jogada 2: ")

# te - Tesoura 
# pa - Papel
# pe - Pedra

if jogada_1 == jogada_2:
    print("Empate")
elif (jogada_1 == "te" and jogada_2 == "pa") or (jogada_1 == "pe" and jogada_2 == "te") or (jogada_1 == "pa" and jogada_2 == "pe"):
    print("J1 venceu!")
else:
    print("J2 venceu!")