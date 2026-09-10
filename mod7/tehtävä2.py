import random

x = int(input("Anna nopan tahkojen määrä: "))
def noppa(x):
    return random.randint(1, x)

while True:
    heitto = noppa(x)
    print(f"Heitit {heitto}.")
    if heitto == x:
        print(f"Onneksi olkoon! Heitit {x}.")
        break