#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan
# euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on
# alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def pizzalaskuri(koko3,hinta3):
    koko3 = koko3 / 100
    tulos = hinta3/(math.pi * (koko3 / 2) ** 2)
    return tulos
koko1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
koko2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))


if pizzalaskuri(koko1,hinta1) < pizzalaskuri(koko2,hinta2):
    print(f"Ensimmäinen pizza on halvempi halvempi ({pizzalaskuri(koko1,hinta1): .4f} €/m^2 vert. {pizzalaskuri(koko2,hinta2): .4f} €/m^2")
else:
    print(f"Toinen pizza on halvempi halvempi ({pizzalaskuri(koko2,hinta2): .4f} €/m^2 vert. {pizzalaskuri(koko1,hinta1): .4f} €/m^2)")