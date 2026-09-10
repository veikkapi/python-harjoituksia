numero = int(input("Anna kokonaisluku: "))

alkuluku = True
if numero < 2:
    alkuluku = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            alkuluku = False
            break

if alkuluku:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")