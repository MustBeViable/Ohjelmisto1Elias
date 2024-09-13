#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos
# nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton
# nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton
# nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee
# 'sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä
# päivittää.

class Auto:
    def __init__(self, PlateNumber, MaxSpeed):
        self.PlateNumber = PlateNumber
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = 0
        self.TravelledDistance = 0
    def Accele(self, Accelerate):
        self.Accelerate = Accelerate
        if float(Accelerate) > 0:
            self.CurrentSpeed += Accelerate
            if self.CurrentSpeed >= self.MaxSpeed:
                self.CurrentSpeed = self.MaxSpeed
        elif float(Accelerate) < 0:
            self.CurrentSpeed += Accelerate
            if self.CurrentSpeed < 0:
                self.CurrentSpeed = 0
        else:
            pass
ferrari = Auto('ABC-123', 142)
print(f"Rekisteritunnus {ferrari.PlateNumber}, huippunopeus {ferrari.MaxSpeed}, nykynen nopeus {ferrari.CurrentSpeed}")
Accelerate = ferrari.Accele(30)
print(f"Rekisteritunnus {ferrari.PlateNumber}, huippunopeus {ferrari.MaxSpeed}, nykynen nopeus {ferrari.CurrentSpeed}")
Accelerate = ferrari.Accele(70)
print(f"Rekisteritunnus {ferrari.PlateNumber}, huippunopeus {ferrari.MaxSpeed}, nykynen nopeus {ferrari.CurrentSpeed}")
Accelerate = ferrari.Accele(50)
print(f"Rekisteritunnus {ferrari.PlateNumber}, huippunopeus {ferrari.MaxSpeed}, nykynen nopeus {ferrari.CurrentSpeed}")