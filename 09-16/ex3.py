p1 = input("Primeira palavra: ").replace("áé", "ae").lower()
p2 = input("Segunda palavra: ").replace("áé", "ae").lower()

h1 = {}
for char in p1:
    if not char in h1:
        h1[char] = 0
    h1[char] += 1 

h2 = {}
for char in p2:
    if not char in h2:
        h2[char] = 0
    h2[char] += 2

if h1 == h2:
    print("Anagrama!")
else:
    print("NÃO!!!!! PARE!!!!!")