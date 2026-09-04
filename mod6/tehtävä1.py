import random
yhteensä = 0
heitot = int(input("Kuinka monta kertaa haluat heittää noppaa? "))
for i in range(heitot):
    noppa = random.randint(1, 6)
    tulos = str(noppa)
    yhteensä += noppa
    print("Heitit: " + tulos)
print("Yhteensä: " + str(yhteensä))
