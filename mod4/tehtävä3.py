sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "mies" or sukupuoli == "Mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on liian korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
if sukupuoli == "nainen" or sukupuoli == "Nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on liian alhainen.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on liian korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
if sukupuoli != "mies" and sukupuoli != "nainen" and sukupuoli != "Mies" and sukupuoli != "Nainen":
    print("Virheellinen biologinen sukupuoli.")