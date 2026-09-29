import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    
    def kiihdyta(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.kuljettu_matka += self.nopeus

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta()
            auto.kulje()

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"Rekisteritunnus: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus} Kuljettu matka {auto.kuljettu_matka}")
    
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(0, 10):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

ralli = Kilpailu("Suuri romuralli", 8000, autot)

hours = 0
while not ralli.kilpailu_ohi():
    ralli.tunti_kuluu()
    hours += 1
    if hours % 10 == 0:
        ralli.tulosta_tilanne()

ralli.tulosta_tilanne()