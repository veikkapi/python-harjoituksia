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

# pelaajan luonti, liikkuminen, esineiden kerääminen ja näyttäminen

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Siirryit huoneeseen: {huone.nimi}")

    def kerää_esine(self, esine):
        if esine in self.sijainti.esineet:
            self.sijainti.poista_esine(esine)
            self.esineet.append(esine)
            print(f"Keräsit esineen: {esine.nimi}")
        else:
            print("Tässä huoneessa ei ole kyseistä esinettä.")

    def nayta_esineet(self):
        if not self.esineet:
            print("Sinulla ei ole esineitä.")
        else:
            print("Hallussasi olevat esineet:")
            for esine in self.esineet:
                print(f"- {esine}")


