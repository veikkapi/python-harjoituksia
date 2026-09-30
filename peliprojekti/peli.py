print("Tervetuloa peliin!")

#pelaaja tiedot (nimi ja ikä)
nimi = input("Mikä on nimesi? ")

while nimi == "":
    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
    nimi = input("Mikä on nimesi? ")

ika = int(input("Kuinka vanha olet? "))

while ika < 0:
    print("Ikä ei voi olla negatiivinen. Yritä uudelleen.")
    ika = int(input("Kuinka vanha olet? "))

if ika < 18:
    print("Olet liian nuori pelaamaan tätä peliä.")
    print("Peli päättyy, häivy.")
    quit()
else:
    print("Tiedot talennettu.")

#päävalikko ja komennot
print("Päävalikko:")
komento = input("Anna komento: ")

while komento != "aloita":

    if komento == "":
        print("Komento ei voi olla tyhjä. Yritä uudelleen.")
        print("Jos et tiedä mitä tehdä, kirjoita 'komennot' nähdäksesi komennot.")
        komento = input("Anna komento: ")

    elif komento == "komennot":
        print("--------------------")
        print("Komennot:")
        print("komennot - näyttää komennot")
        print("aloita - aloittaa pelin")
        print("poistu - keskeyttää pelin")
        print("yllätys - et uskalla")
        print("tiedot - näyttää tietosi")
        print("--------------------")
        komento = input("Anna komento: ")


    elif komento == "poistu":
        print("Peli keskeytetty.")
        quit()

    elif komento == "yllätys":
        print("Yllätys! Hävisit pelin.")
        quit()

    elif komento == "tiedot":
        print("Tiedot:")
        print(f"Nimi: {nimi}")
        print(f"Ikä: {ika}")
        komento = input("Anna komento: ")

    elif komento != "komennot" and komento != "poistu" and komento != "yllätys" and komento != "tiedot":
        print("Tuntematon komento. Yritä uudelleen.")
        komento = input("Anna komento: ")

#tästä alkaa itse peli

print("--------------------")
print("Intro:")
print("")

tavarat = []
tavara = input("Mitä pakataan? (tyhjä lopettaa):")

while tavara != "":

    if tavara not in tavarat:
        print(f"{tavara} on nyt pakattu.")

    if tavara in tavarat:
        print("Tämä on pakattu jo.")

    tavarat.append(tavara)
    tavara = input("Mitä pakataan? (tyhjä lopettaa):")
