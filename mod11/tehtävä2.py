class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus)
        

    def aja(self, x):
        matkamittari = self.huippunopeus * x
        print(f"Auto {self.rekisteritunnus} ajoi {matkamittari} kilometriä {x} tunnissa.")


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akun_kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akun_kapasiteetti = int(akun_kapasiteetti)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = int(bensatankin_koko)

auto1 = Sähköauto("ABC_15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD_123", 165, 32.3)
auto1.aja(3)
auto2.aja(3)

