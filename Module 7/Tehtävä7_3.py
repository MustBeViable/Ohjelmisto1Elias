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
def kysymys():
    kyssari = input(
        "Jos haluat tallentaa uudet lentoasemantiedot, kirjoita 1. Jos haluat tarkastaa lentoaseman tiedot, "
        "kirjoita 2. Lopettaaksesi paina ENTER: ")
    return kyssari
tulos = kysymys()
while tulos:
    if int(tulos) == 1:
        asema1 = input("Anna lentoaseman nimi: ")
        ICAO1 = input("Anna ICAO: ")
        lentoas(asema1,ICAO1)
        tulos = kysymys()
    elif int(tulos) == 2:
        num = input("Kerro hakemasi aseman nimi: ")
        print(f"Aseman {num} ICAO koodi on {lentoasemat[num]}")
        tulos = kysymys()
else:
    print("Kiitti moi")
    print(lentoasemat)