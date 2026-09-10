nimet = {""}
nimi = input("Kirjoita nimi: ")

while nimi != "":

    if nimi not in nimet:
        print("Uusi nimi.")

    if nimi in nimet:
        print("Aiemmin käytetty nimi.")

    nimet.add(nimi)
    nimi = input("Kirjoita nimi: ")

for nimi in nimet:
    print(nimi)

