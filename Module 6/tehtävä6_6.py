#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan
# euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on
# alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def pizzalaskuri(koko3,hinta3):
    koko3 = koko3 / 100
    tulos = hinta3/(math.pi * (koko3 / 2) ** 2)
    return tulos
koko1 = float(input("Anna koko1: "))
koko2 = float(input("Anna koko2: "))
hinta1 = float(input("Anna hinta1: "))
hinta2 = float(input("Anna hinta2: "))

print(pizzalaskuri(koko1,hinta1))
print(pizzalaskuri(koko2,hinta2))

if pizzalaskuri(koko1,hinta1) < pizzalaskuri(koko2,hinta2):
    print("Pizza 1 halvempi")
else:
    print("Pizza 2 halvempi")