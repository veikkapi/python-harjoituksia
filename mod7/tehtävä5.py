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


def KarsiParittomat():
    return [luku for luku in kokonaisluvut if luku % 2 != 0]

lukuja()
parittomat = KarsiParittomat()
print(f"Lista ilman parillisia lukuja: {parittomat}")

