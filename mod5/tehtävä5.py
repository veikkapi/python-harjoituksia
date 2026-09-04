käyttäjätunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
yritykset = 0

while käyttäjätunnus != "python" or salasana != "rules":
    yritykset += 1
    if yritykset >= 5:
        print("Pääsy evätty.")
        break
    print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
else:
    print("Tervetuloa!")