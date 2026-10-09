from pathlib import Path

BUDJETTI = 1000
LAHTOPAIKKA = "Kilo, Espoo, Suomi"
NAYTA_PAASTOT = True             # näyttää päästöt yhteensä pelin aikana
NAYTA_VALINTOJEN_PAASTOT = False  # näyttää päästöt myös jokaisen valinnan kohdalla

# ---------- apufunktiot ----------

def poikkiviiva(): #tein tämän funktion, koska en jaksanut kirjoittaa joka kerta print koodia.
    print("--------------------")


def kysy_kokonaisluku(kehote): #palauttaa kokonaisluvun, jos syöte ei ole kokonaisluku, pyytää uudelleen.
    while True:
        try:
            return int(input(kehote))
        except ValueError:
            print("Anna luku numeroina.")


def laske_arvosana(paastot_g): # laskee arvosanan CO2-päästöjen perusteella. Palauttaa tuple (arvosana, viesti).
    #päästöt grammoina
    if paastot_g <= 2000:
        return "A+", "Täydellistä!"
    elif paastot_g <= 5000:
        return "A", "Mahtavaa!"
    elif paastot_g <= 10000:
        return "B", "Hyvä!"
    elif paastot_g <= 25000:
        return "C", "Tyydyttävä."
    elif paastot_g <= 50000:
        return "D", "Välttävä."
    elif paastot_g <= 100000:
        return "D-", "Huono."
    else:
        return "F", "Ei näin…"


def muokkaa_tietoja(nimi, ika):
#Antaa pelaajan vaihtaa nimen ja iän. Tyhjä syöte ei muuta mitään.
    poikkiviiva()
    print("Tietojen muokkaus (jätä kenttä tyhjäksi, jos et halua muuttaa sitä)")

    uusi_nimi = input(f"Uusi nimi (nyt {nimi}): ").strip()
    if uusi_nimi != "":
        nimi = uusi_nimi

    while True:
        syote = input(f"Uusi ikä (nyt {ika}): ").strip()
        if syote == "":
            break
        try:
            uusi_ika = int(syote)
        except ValueError:
            print("Anna ikä numerona.")
            continue
        if uusi_ika < 0:
            print("Ikä ei voi olla negatiivinen. Yritä uudelleen.")
            continue
        if uusi_ika < 12:
            print("Olet liian nuori pelaamaan tätä peliä.")
            print("Peli päättyy, häivy.")
            quit()
        ika = uusi_ika
        break

    print("Tiedot päivitetty.")
    return nimi, ika


# ---------- luokat ----------

class Pelaaja:
    def __init__(self, nimi, ika, sijainti):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.saldo = BUDJETTI
        self.paastot = 0


# ---------- reittidata ----------
# Jokainen solmu on paikka matkan varrella. "valinnat" kertoo, mihin
# solmuun voi siirtyä, ja paljonko se maksaa (€) ja päästää (g CO2).
# Solmu, jossa on "loppu": True, on perille pääsy.

PERILLA = {"loppu": True, "kuvaus": "Saavuit perille!"}


def lento(teksti, hinta, paastot):
    return {"teksti": teksti, "seuraava": "perilla", "hinta": hinta, "paastot": paastot}


def matkakartta(lennot):
    """Kilosta Helsinki-Vantaan lentokentälle ja sieltä lentäen kohteeseen."""
    return {
        "alku": {
            "kuvaus": f"Olet paikassa {LAHTOPAIKKA} ja lomamatkasi alkaa.",
            "valinnat": [
                {"teksti": "Lähijuna Leppävaaraan", "seuraava": "leppavaara", "hinta": 3, "paastot": 100},
                {"teksti": "Lähijuna Helsingin päärautatieasemalle", "seuraava": "helsinki_keskusta", "hinta": 5, "paastot": 300},
                {"teksti": "Taksi suoraan lentokentälle", "seuraava": "lentokentta", "hinta": 85, "paastot": 7000},
            ],
        },
        "leppavaara": {
            "kuvaus": "Olet Leppävaaran asemalla.",
            "valinnat": [
                {"teksti": "Lentokenttäjuna", "seuraava": "lentokentta", "hinta": 5, "paastot": 300},
                {"teksti": "Taksi lentokentälle", "seuraava": "lentokentta", "hinta": 45, "paastot": 5000},
            ],
        },
        "helsinki_keskusta": {
            "kuvaus": "Olet Helsingin päärautatieasemalla.",
            "valinnat": [
                {"teksti": "Lentokenttäjuna", "seuraava": "lentokentta", "hinta": 5, "paastot": 300},
                {"teksti": "Taksi lentokentälle", "seuraava": "lentokentta", "hinta": 55, "paastot": 6000},
            ],
        },
        "lentokentta": {
            "kuvaus": "Olet Helsinki-Vantaan lentokentällä.",
            "valinnat": lennot,
        },
        "perilla": PERILLA,
    }


def matka_tampere():
    return {
        "alku": {
            "kuvaus": f"Olet paikassa {LAHTOPAIKKA} ja lomamatkasi alkaa.",
            "valinnat": [
                {"teksti": "Lähijuna Helsingin päärautatieasemalle", "seuraava": "helsinki_asema", "hinta": 5, "paastot": 300},
                {"teksti": "Kaukobussi Tampereelle", "seuraava": "perilla", "hinta": 20, "paastot": 7000},
                {"teksti": "Kimppakyyti Tampereelle", "seuraava": "perilla", "hinta": 18, "paastot": 9000},
                {"teksti": "Oma auto", "seuraava": "perilla", "hinta": 45, "paastot": 28000},
                {"teksti": "Taksi Tampereelle", "seuraava": "perilla", "hinta": 280, "paastot": 30000},
            ],
        },
        "helsinki_asema": {
            "kuvaus": "Olet Helsingin päärautatieasemalla.",
            "valinnat": [
                {"teksti": "Kaukojuna Tampereelle", "seuraava": "perilla", "hinta": 25, "paastot": 1500},
                {"teksti": "Kaukojuna, 1. luokka", "seuraava": "perilla", "hinta": 45, "paastot": 1500},
                {"teksti": "Taksi Tampereelle", "seuraava": "perilla", "hinta": 300, "paastot": 30000},
            ],
        },
        "perilla": PERILLA,
    }


def matka_tallinna():
    kartta = matkakartta([
        lento("Lento Tallinnaan", 150, 20000),
        lento("Lento Tallinnaan, business-luokka", 380, 45000),
    ])
    kartta["alku"]["valinnat"].append(
        {"teksti": "Taksi suoraan Länsiterminaali 2:lle", "seuraava": "lansiterminaali", "hinta": 45, "paastot": 5000}
    )
    kartta["helsinki_keskusta"]["valinnat"] += [
        {"teksti": "Ratikka Länsiterminaali 2:lle", "seuraava": "lansiterminaali", "hinta": 3, "paastot": 150},
        {"teksti": "Taksi Länsiterminaali 2:lle", "seuraava": "lansiterminaali", "hinta": 30, "paastot": 1500},
    ]
    kartta["lansiterminaali"] = {
        "kuvaus": "Olet Länsiterminaali 2:lla.",
        "valinnat": [
            {"teksti": "Laiva, edullinen lippu", "seuraava": "perilla", "hinta": 30, "paastot": 12000},
            {"teksti": "Laiva, hyttimatka", "seuraava": "perilla", "hinta": 120, "paastot": 12000},
        ],
    }
    return kartta


def matka_bergen():
    return matkakartta([
        lento("Edullinen lento vaihdolla", 130, 260000),
        lento("Suora lento", 220, 190000),
        lento("Business-luokka", 950, 480000),
    ])


def matka_munchen():
    return matkakartta([
        lento("Edullinen lento vaihdolla", 120, 240000),
        lento("Suora lento", 180, 190000),
        lento("Business-luokka", 950, 450000),
    ])


def matka_chania():
    return matkakartta([
        lento("Edullinen lento vaihdolla", 220, 420000),
        lento("Suora lento", 330, 330000),
        lento("Business-luokka", 1100, 800000),
    ])


def matka_barcelona():
    return matkakartta([
        lento("Edullinen lento vaihdolla", 190, 430000),
        lento("Suora lento", 280, 360000),
        lento("Business-luokka", 1100, 850000),
    ])


def matka_agia_napa():
    return matkakartta([
        lento("Edullinen lento vaihdolla", 260, 500000),
        lento("Suora lento", 380, 420000),
        lento("Business-luokka", 1300, 950000),
    ])

# ---------- kohteiden introt ----------

def odota(): # olisin halunnut lisää tämän intro ja ohjeet tekstiin, mutta en saanut sitä toimimaan. Joten jätin sen pois.
    input("\n[Paina Enter jatkaaksesi]")


def intro_tampere():
    print("Hyvä valinta! Kotimainen matkakohde, joka on täynnä kulttuuria ja kauniita maisemia.")
    print("Kuulin, että Särkänniemi on vielä auki syksyllä Karmivan Halloweenin aikaan, joten sinne on pakko päästä!")
    odota()
    print("Et ole myöskään nähnyt kavereita pitkään aikaan heidän muuttaessaan opiskelemaan uuteen kaupunkiin.")
    print("Nyt on aika lähteä tapaamaan heitä ja viettämään hauskaa viikonloppua Tampereelle!")


def intro_tallinna():
    print("Hienoa! Tallinna on upea kohde, jossa yhdistyvät historia ja moderni kaupunkielämä.")
    print("Vanhakaupunki ei ikinä petä, ja siellä on paljon nähtävää ja koettavaa.")
    odota()
    print("Risteily Tallinnaan on suosittu tapa viettää viikonloppua.")
    print("Lentäminen on myös toinen tapa päästä perille, kalliimpi, mutta nopeampi. Valinta on sinun!")


def intro_bergen():
    print("Upea valinta! Bergen on Norjan toiseksi suurin kaupunki, joka tunnetaan kauniista vuonoistaan.")
    print("Lähistöllä sijaitsevat vuoret tarjoavat upeat mahdollisuudet patikointiin ja ulkoiluun, sekä kokemaan upeita maisemia vuonojen kera.")
    odota()
    print("Kaupungin värikkäät puutalot ja satama-alue tekevät siitä viehättävän kohteen.")
    print("Bergen tunnetaan myös upeista kirkoistaan ja museoistaan, joten kulttuurielämyksiä on tarjolla runsaasti.")
    print("Muista pakata lämpimät vaatteet nyt syksyllä!")
    

def intro_munchen():
    print("Oktoberfestin aikaan München on täynnä elämää ja juhlaa!")
    print("Kaupungin historialliset rakennukset ja kauniit puistot tekevät siitä viehättävän kohteen.")
    odota()
    print("München on myös tunnettu hyvistä ravintoloistaan ja kahviloistaan, joten ruokailu on erinomaista.")
    print("Älä juo liikaa olutta, sillä se voi vaikuttaa matkabudjettiisi!")


def intro_chania():
    print("Suomalaisille tuttu lomakohde Kreikka on varsin tunnettu, mutta Chaniá on hieman tuntemattomampi.")
    print("Chaniá on viehättävä kaupunki, joka sijaitsee Kreetan saarella.")
    odota()
    print("Kreetan saari on tunnettu upeista rannoistaan, historiallisista kohteistaan ja herkullisesta ruoastaan.")
    print("Kreikan syksy tarjoaa vielä lämpimiä hellepäiviä, joten voit vielä nauttia auringosta ja merestä!")


def intro_barcelona():
    print("Barcelona on Espanjan kulttuurinen helmi, joka tarjoaa upeita nähtävyyksiä ja elämää täynnä olevia katuja.")
    print("Kaupungin arkkitehtuuri, erityisesti Gaudín teokset, ovat maailmankuuluja.")
    print("Samoin upea kirkko Sagrada Família on ehdottomasti jokaisen nähtävä.")
    odota()
    print("Kaupunki kotouttaa myös tunnettuja jalkapallojoukkueita, kuten FC Barcelona, joten urheilun ystäville on paljon nähtävää ja koettavaa.")    
    print("Stadioni Camp Nou on ehdottomasti vierailun arvoinen.")


def intro_agia_napa():
    print("Agia Napa on Kyproksen tunnetuin lomakohde, joka tarjoaa upeita rantoja ja vilkasta yöelämää.")
    odota()
    print("Kaupungin kauniit hiekkarannat ja kirkas turkoosi meri tekevät siitä täydellisen paikan rentoutumiseen ja auringonottoon.")
    print("Agia Napa on hieman kallis, mutta mitä parempaa lomaa voi toivoa kuin aurinkoa, merta ja biletystä!")


KOHTEET = {
    "tampere": {
        "nimi": "Tampere, Suomi",
        "intro": intro_tampere,
        "kartta": matka_tampere(),
    },
    "tallinna": {
        "nimi": "Tallinna, Viro",
        "intro": intro_tallinna,
        "kartta": matka_tallinna(),
    },
    "bergen": {
        "nimi": "Bergen, Norja",
        "intro": intro_bergen,
        "kartta": matka_bergen(),
    },
    "munchen": {
        "nimi": "München, Saksa",
        "intro": intro_munchen,
        "kartta": matka_munchen(),
    },
    "chania": {
        "nimi": "Chaniá, Kreikka",
        "intro": intro_chania,
        "kartta": matka_chania(),
    },
    "barcelona": {
        "nimi": "Barcelona, Espanja",
        "intro": intro_barcelona,
        "kartta": matka_barcelona(),
    },
    "agia_napa": {
        "nimi": "Agia Napa, Kypros",
        "intro": intro_agia_napa,
        "kartta": matka_agia_napa(),
    },
}


# ---------- pelilogiikka ----------

def pelaa_polku(pelaaja, kartta):
    """Pelaa reitin alusta loppuun. Palauttaa True, jos pääsit perille."""
    solmu = "alku"

    while True:
        tiedot = kartta[solmu]
        poikkiviiva()
        print(tiedot["kuvaus"])

        if tiedot.get("loppu"):
            return True

        valinnat = tiedot["valinnat"]
        print(f"Saldo: {pelaaja.saldo:.2f} €")
        if NAYTA_PAASTOT:
            print(f"Päästöt tähän mennessä: {pelaaja.paastot} g CO2")

        for i, v in enumerate(valinnat, start=1):
            rivi = f"{i}. {v['teksti']} - {v['hinta']} €"
            if NAYTA_VALINTOJEN_PAASTOT:
                rivi += f" | {v['paastot']} g CO2"
            print(rivi)

        numero = kysy_kokonaisluku("Valitse numero: ")
        while numero < 1 or numero > len(valinnat):
            print("Valitse numero listalta.")
            numero = kysy_kokonaisluku("Valitse numero: ")

        valinta = valinnat[numero - 1]
        pelaaja.saldo -= valinta["hinta"]
        pelaaja.paastot += valinta["paastot"]
        pelaaja.sijainti = valinta["seuraava"]

        if pelaaja.saldo < 0:
            print(f"Budjettisi ylittyi ({pelaaja.saldo:.2f} €). Hävisit pelin.")
            return False

        solmu = valinta["seuraava"]


# ---------- pelaajan tiedot ----------

nimi = input("Mikä on nimesi? ")
while nimi == "":
    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
    nimi = input("Mikä on nimesi? ")

ika = kysy_kokonaisluku("Kuinka vanha olet? ")
while ika < 0:
    print("Ikä ei voi olla negatiivinen. Yritä uudelleen.")
    ika = kysy_kokonaisluku("Kuinka vanha olet? ")

if ika < 12:
    print("Olet liian nuori pelaamaan tätä peliä.")
    print("Peli päättyy, häivy.")
    quit()
else:
    print("Tiedot tallennettu.")


# ---------- päävalikko ----------

poikkiviiva()
print("Päävalikko:")
print("Kirjoita 'komennot' nähdäksesi komennot.")
while True:
    komento = input("Anna komento: ").strip().lower()

    if komento == "aloita":
        break
    elif komento == "":
        print("Komento ei voi olla tyhjä. Kirjoita 'komennot' nähdäksesi komennot.")
    elif komento == "komennot":
        poikkiviiva()
        print("Komennot:")
        print("komennot - näyttää komennot")
        print("aloita - aloittaa pelin")
        print("poistu - keskeyttää pelin")
        print("tiedot - näyttää tietosi")
        print("tietojen muokkaus - muuttaa nimesi ja ikäsi")
        poikkiviiva()
    elif komento == "poistu":
        print("Peli keskeytetty.")
        quit()
    elif komento == "tiedot":
        print("Tiedot:")
        print(f"Nimi: {nimi}")
        print(f"Ikä: {ika}")
        print(f"Lähtöpaikka: {LAHTOPAIKKA}")
    elif komento == "tietojen muokkaus":
        nimi, ika = muokkaa_tietoja(nimi, ika)
    else:
        print("Tuntematon komento. Yritä uudelleen.")


# ---------- itse peli ----------

pelaaja = Pelaaja(nimi, ika, LAHTOPAIKKA)

poikkiviiva() #introtekstin tiedostonkäsittely
intro_polku = Path(__file__).parent / "intro.txt"
try:
    print(intro_polku.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("(intro.txt-tiedostoa ei löytynyt)")

poikkiviiva() #ohjetekstin tiedostonkäsittely
ohje_polku = Path(__file__).parent / "ohje.txt"
try:
    print(ohje_polku.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("(ohje.txt-tiedostoa ei löytynyt)")

# kohteen valinta
poikkiviiva()
print("Lomakohteet:")
kohteet = list(KOHTEET.values())
for i, k in enumerate(kohteet, start=1):
    print(f"{i}. {k['nimi']}")

numero = kysy_kokonaisluku("Minne haluat matkustaa? Valitse numero: ")
while numero < 1 or numero > len(kohteet):
    print("Valitse numero listalta.")
    numero = kysy_kokonaisluku("Minne haluat matkustaa? Valitse numero: ")
kohde = kohteet[numero - 1]

# kohteen intro
poikkiviiva()
print(f"Valitsit kohteen: {kohde['nimi']}")
poikkiviiva()
kohde["intro"]()

# matkustaminen kohteeseen ja lopputulos
if pelaa_polku(pelaaja, kohde["kartta"]):
    arvosana, viesti = laske_arvosana(pelaaja.paastot)
    poikkiviiva()
    print(f"Onneksi olkoon {pelaaja.nimi}, pääsit kohteeseen {kohde['nimi']}!")
    print(f"Jäljellä oleva saldo: {pelaaja.saldo:.2f} €")
    print(f"Päästöt yhteensä: {pelaaja.paastot} g CO2")
    print(f"Arvosana: {arvosana} - {viesti}")