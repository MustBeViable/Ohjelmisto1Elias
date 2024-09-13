#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden
# auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton
# (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.


class Auto:
    def __init__(self, PlateNumber, MaxSpeed):
        self.PlateNumber = PlateNumber
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = 0
        self.TravelledDistance = 0
ferrari = Auto('ABC-123', 142)
print(f"Rekisteritunnus {ferrari.PlateNumber}, huippunopeus {ferrari.MaxSpeed}")