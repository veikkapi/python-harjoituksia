print("Tervetuloa peliin!")

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

print("Päävalikko:")
komento = input("Anna komento: ")

while komento != "lopeta":

    if komento == "":
        print("Komento ei voi olla tyhjä. Yritä uudelleen.")
        print("Jos et tiedä mitä tehdä, kirjoita 'komennot' nähdäksesi komennot.")
        komento = input("Anna komento: ")

    elif komento == "komennot":
        print("Komennot:")
        print("komennot - näyttää komennot")
        print("lopeta - jatkaa peliä")
        print("poistu - keskeyttää pelin")
        print("yllätys - et uskalla")
        print("tiedot - näyttää tietosi")
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

print("Aloitetaan peli!")

