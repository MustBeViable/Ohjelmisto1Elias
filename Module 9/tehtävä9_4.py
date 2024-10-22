#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa
# lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h
# ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana
# tehdään tunnin välein seuraavat toimenpiteet:

"""
- Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.

- Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""
import random


class Auto:
    def __init__(self, Name, PlateNumber, MaxSpeed):
        self.Name = Name
        self.PlateNumber = PlateNumber
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = 0
        self.TravelledDistance = 0
    def accele(self, Accelerate):
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
    def move(self, hour):
        self.TravelledDistance += self.CurrentSpeed * hour
    def __str__(self):
        return f"{self.Name}"

cars = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7", "auto8", "auto9", "auto10"]

for i in range(len(cars)):
    cars[i] = Auto(cars[i],"ABC-"+ str(i + 1), random.randint(100,200))
race_over = False

while race_over == False:
    for i in range(len(cars)):
        cars[i].accele(random.randint(-15, 10))
        cars[i].move(1)
    for i in range(len(cars)):
        if cars[i].TravelledDistance >= 10000:
            race_over = True
print("Auto, rekisterinumero, huippunopeus, kokonaismatka")
for i in range(len(cars)):
    print(f"{cars[i]}.   {cars[i].PlateNumber} | {cars[i].MaxSpeed:4.0f} | {cars[i].TravelledDistance:4.0f}")