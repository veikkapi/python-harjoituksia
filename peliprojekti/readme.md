# Peliprojekti

**Veikka Pietiäinen**

## Juoni

Syysloma yllättää etkä ole kiireisen arjen takia kerennyt suunnittelemaan mitään ihmeellistä.
Kova työ on kuitenkin palkittava, joten nyt on aika lähteä!
Varo ettet kuitenkaan ylitä budjettiasi.


## Toiminnallisuus

1 - Alussa määritellään asetukset ja funktiot. Näitä ovat BUDJETTI, LAHTOPAIKKA ja päästöjen näyttöasetukset sekä apufunktiot, Pelaaja-luokka ja reittidata.

2 - Pelaajan tiedot kysytään. Nimi ei saa olla tyhjä. Ikä kysytään kysy_kokonaisluku-funktiolla, joka pyytää uudelleen, jos syöte ei ole luku. Alle 12-vuotias saa pelin päättymään quit()-kutsulla.

3 - Päävalikko pyörii while True -silmukassa. Komennot ovat komennot, tiedot, tietojen muokkaus, poistu ja aloita. Vain aloita rikkoo silmukan (break) ja vie peliin.

4 - Peli alkaa. Luodaan Pelaaja-olio, jonkaa on saldo (1000 €) ja päästöt (0 g). Sen jälkeen tulostetaan intro.txt ja ohje.txt tiedostoista. Jos tiedostoa ei löydy, try/except näyttää virheen kaatumisen sijaan.

5 - Kohteet tulostetaan numeroituna listana KOHTEET-sanakirjasta. Valinnan jälkeen ajetaan kohteen intro-funktio, jossa odota() pysäyttää tekstin Enterin painallukseen.

6 - pelaa_polku() pelaa reitin läpi ja palauttaa True tai False. Jokainen valinta vähentää saldoa ja lisää päästöjä.

7 - Lopputulos. Perille päästyäsi tulostuvat saldo, päästöt ja arvosana.


## Kestävä kehitys pelissä

Pelin teema on suunniteltu kestävän kehityksen tavoite 13.3 ympärille, joka kuulu näin:

"Parantaa ilmastonmuutoksen hidastamiseen, sopeutumiseen, vaikutusten lievittämiseen
ja ennakkovaroituksiin liittyvää koulutusta, tietämyksen lisäämistä
sekä kansalaisten ja instituutioiden valmiuksia."

Pelin tavoitteena on tuoda esiin matkustamisen ja lomamatkojen aiheutumat haitalliset päästöt.
Tavoitteena ei ole kuitenkaan kokonaan kieltää lomailu vaan saada ihmiset olemaan harkitsevaisempia
valitsemistaan matkailutavoista ja vähentämään ympäristölle sekä ilmastolle haitallisia CO2-päästöjä.