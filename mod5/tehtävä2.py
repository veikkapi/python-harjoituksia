tuuma = float(input("Anna tuumien lukumäärä: "))
sentti = tuuma * 2.54
while tuuma >= 0:
    if tuuma < 0:
        break
    print(f"{tuuma} tuumaa on {sentti} senttimetriä.")
    tuuma = float(input("Anna tuumien lukumäärä: "))
    sentti = tuuma * 2.54
