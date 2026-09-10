kokonaisluvut = []

def lukuja():
    while True:
        luku = input("Anna kokonaisluku (tyhjä lopettaa): ")
        if luku == "":
            break
        try:
            kokonaisluvut.append(int(luku))
        except ValueError:
            print("Virheellinen syöte. Anna kokonaisluku.")

lukuja()
print(f"Annetut luvut: {kokonaisluvut}")
print(f"Summa: {sum(kokonaisluvut)}")