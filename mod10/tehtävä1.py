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
        if self.kerros + 1 <= self.ylin_kerros:
            self.kerros = self.ylin_kerros
        else:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa: {self.kerros}")
    def siirry_alas(self):
        if self.kerros - 1 <= self.alin_kerros:
            self.kerros = self.alin_kerros
        else:    
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa: {self.kerros}")

h = Hissi(1, 5)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)