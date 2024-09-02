#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
# syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden
# lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
# ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman
# suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän
# haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi
# on EFHK. Löydät koodeja helposti selaimen avulla.)
lentoasemat = {}
def lentoas(asema,ICAO):
    lentoasemat[asema] = ICAO
    return lentoasemat
def kysymys(kys):
    kyssari = input(
        "Jos haluat tallentaa uudet lentoasemantiedot, kirjoita TIEDOT. Jos haluat tarkastaa lentoaseman tiedot, "
        "kirjoita TARKASTA. Lopettaaksesi paina ENTER: ")
    return kyssari
tulos = kysymys(hei)
print(tulos)
print(kysymys(hei))
if tulos == TIEDOT:
    asema1 = input("Anna: ")
    ICAO1 = input("Anna ICAO: ")
    lentoas(asema1,ICAO1)
    kysymys()
elif tulos == TARKISTA:
    num = input("Kerro hakemasi aseman nimi: ")
    print(f"Aseman {num} ICAO koodi on {lentoasemat[num]}")
    kysymys()
elif not tulos:
    print("")
else:
    print("Tarkista antamasi syöte!")
    kysymys()