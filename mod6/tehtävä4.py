kaupungit = []

kaupunki = input("Kirjoita kaupungin nimi: ")
while kaupunki != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Kirjoita kaupungin nimi: ")

for kaupunki in kaupungit:
    print(kaupunki)