class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto1 = Auto("ABC-123", 142, 0, 0)

print("Auto 1:")
print("Rekisteritunnus:", auto1.rekisteritunnus)
print("Huippunopeus:", auto1.huippunopeus)
print("Tämänhetkinen nopeus:", auto1.tämänhetkinen_nopeus)
print("Kuljettu matka:", auto1.kuljettu_matka)