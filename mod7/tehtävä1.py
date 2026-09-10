import random

def noppa():
    return random.randint(1, 6)

while True:
    heitto = noppa()
    print(f"Heitit {heitto}.")
    if heitto == 6:
        print("Onneksi olkoon! Heitit kuusi.")
        break