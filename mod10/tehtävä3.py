class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if self.kerros < kerros:
                self.siirry_ylos()
            elif self.kerros > kerros:
                self.siirry_alas()

    def siirry_ylos(self):
        if self.kerros >= self.ylin_kerros:
            self.kerros = self.ylin_kerros
        else:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa: {self.kerros}")

    def siirry_alas(self):
        if self.kerros <= self.alin_kerros:
            self.kerros = self.alin_kerros
        else:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa: {self.kerros}")

    def palohälytys(self):
        self.kerros = self.alin_kerros
        print(f"Palohälytys! Hissi on nyt kerroksessa: {self.kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for _ in range(hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kerros)

talo1 = Talo(1, 10, 3)

talo1.aja_hissiä(2, 4)

for hissi in talo1.hissit:
    hissi.palohälytys()