kuha = float(input("Anna kuhan pituus (cm): "))
if kuha < 37:
    print("Kuhan pituus on " + str(37 - kuha) + " cm liian pieni.")
    print("Laske kuha takaisin järveen.")
if kuha >= 37:
    print("Nyt on hyvä kuha.")
