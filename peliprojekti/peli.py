import json

def poikkiviiva(): #kävi raskaaksi kirjoittaa samaa koodia uudestaan ja uudestaan, joten tein funtion
    print("--------------------")

#pelaaja tiedot (nimi ja ikä)
nimi = input("Mikä on nimesi? ")

while nimi == "":
    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
    nimi = input("Mikä on nimesi? ")

ika = int(input("Kuinka vanha olet? "))

while ika < 0:
    print("Ikä ei voi olla negatiivinen. Yritä uudelleen.")
    ika = int(input("Kuinka vanha olet? "))

if ika < 12:
    print("Olet liian nuori pelaamaan tätä peliä.")
    print("Peli päättyy, häivy.")
    quit()
else:
    print("Tiedot talennettu.")

#päävalikko ja komennot
poikkiviiva()
print("Päävalikko:")
komento = input("Anna komento: ")

while komento != "aloita":

    if komento == "":
        print("Komento ei voi olla tyhjä. Yritä uudelleen.")
        print("Jos et tiedä mitä tehdä, kirjoita 'komennot' nähdäksesi komennot.")
        komento = input("Anna komento: ")

    elif komento == "komennot":
        poikkiviiva()
        print("Komennot:")
        print("komennot - näyttää komennot")
        print("aloita - aloittaa pelin")
        print("poistu - keskeyttää pelin")
        print("yllätys - et uskalla")
        print("tiedot - näyttää tietosi")
        poikkiviiva()
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

# luokat

class Pelaaja:
    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.saldo = 1000
        self.päästöt = 0

class Paikka:
    pass

# pelaajan luonti

pelaaja = Pelaaja(nimi, ika, "koti")
#tästä alkaa itse peli

poikkiviiva()
with open("peliprojekti/intro.txt", "r") as f:
    intro = f.read()
    print(intro)