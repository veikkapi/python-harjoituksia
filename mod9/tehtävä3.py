class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        if self.nopeus + muutos <= 0:
            self.nopeus = 0
        elif self.nopeus + muutos >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += muutos

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + (tunnit*self.nopeus)

auto1 = Auto("ABC-123", 142)
print(auto1.nopeus)
auto1.kiihdyta(30)
auto1.kulje(2)
print(auto1.nopeus)
print(auto1.kuljettu_matka)
