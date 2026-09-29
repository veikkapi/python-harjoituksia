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

auto1 = Auto("ABC-123", 142)
print(auto1.nopeus)
auto1.kiihdyta(30)
print(auto1.nopeus)
auto1.kiihdyta(50)
print(auto1.nopeus)
auto1.kiihdyta(-200)
print(auto1.nopeus)
