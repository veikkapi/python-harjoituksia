import random

numero = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != numero:
    if arvaus < numero:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

print("Oikein!")