luku = input("Kirjoita lukuja (tyhjä rivi lopettaa): ")

pienin = None
suurin = None

while luku != "":
    luku = float(luku)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

    luku = input()


print("Pienin luku on:", pienin)
print("Suurin luku on:", suurin)
