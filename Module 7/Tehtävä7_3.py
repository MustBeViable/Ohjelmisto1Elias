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
        "Jos haluat tallentaa uudet lentoasemantiedot, kirjoita T. Jos haluat tarkastaa lentoaseman tiedot, "
        "kirjoita A. Lopettaaksesi paina ENTER: ")
    return kyssari
hei = 0
tulos = kysymys(hei)
while tulos:
    if tulos == "T":
        print("T1")
        asema1 = input("Anna lentoaseman nimi: ")
        ICAO1 = input("Anna ICAO: ")
        lentoas(asema1,ICAO1)
        kysymys(hei)
    elif tulos == "A":
        print("T2")
        num = input("Kerro hakemasi aseman nimi: ")
        print(f"Aseman {num} ICAO koodi on {lentoasemat[num]}")
        kysymys(hei)
    elif not tulos:
        print("T3")
else:
    print("T4")
    print("Tarkista antamasi syöte!")
    kysymys(hei)