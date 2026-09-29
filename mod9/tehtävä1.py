class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", 142)

print("Auto 1:")
print("Rekisteritunnus:", auto1.rekisteritunnus)
print("Huippunopeus:", auto1.huippunopeus)
print("Tämänhetkinen nopeus:", auto1.tämänhetkinen_nopeus)
print("Kuljettu matka:", auto1.kuljettu_matka)