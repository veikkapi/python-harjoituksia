numerot = []
numero = input("Anna numero: ")

while numero != "":
    if numero.isdigit():
        numerot.append(int(numero))
    else:
        print("Virheellinen syöte. Anna numero tai paina Enter lopettaaksesi.")
    numero = input("Anna numero: ")

if len(numerot) == 0:
    print("Et antanut yhtään numeroa.")
else:
    numerot.sort(reverse=True)
    print("Suurimmat viisi numeroa:")
    for i in range(min(5, len(numerot))):
        print(numerot[i])