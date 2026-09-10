kuukaudet = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu"]
vuoden_ajat = ["talvi", "kevät", "kesä", "syksy"]
numero = int(input("Anna kuukauden numero (1-12): "))
if 1 <= numero <= 12:
    kuukauden_nimi = kuukaudet[numero - 1]
    if numero in [12, 1, 2]:
        vuoden_aika = vuoden_ajat[0]
    elif numero in [3, 4, 5]:
        vuoden_aika = vuoden_ajat[1]
    elif numero in [6, 7, 8]:
        vuoden_aika = vuoden_ajat[2]
    else:
        vuoden_aika = vuoden_ajat[3]
    print(f"Kuukausi on {kuukauden_nimi} ja vuodenaika on {vuoden_aika}.")