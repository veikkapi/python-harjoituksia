vuosiluku = input("Anna vuosiluku: ")
if int(vuosiluku) % 4 == 0 and int(vuosiluku) % 100 != 0 or int(vuosiluku) % 400 == 0:
    print("Vuosi " + str(vuosiluku) + " on karkausvuosi.") 
else:
    print("Vuosi " + str(vuosiluku) + " ei ole karkausvuosi.")