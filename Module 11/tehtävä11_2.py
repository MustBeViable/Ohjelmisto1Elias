#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena
# akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita
# aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja
# akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123,
# 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta
# autojen matkamittarilukemat.
import random

class Auto:
    def __init__(self, name, platenumber, maxspeed):
        self.name = name
        self.platenumber = platenumber
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.travelleddistance = 0
    def accele(self, accelerate):
        if float(accelerate) > 0:
            self.currentspeed += accelerate
            if self.currentspeed >= self.maxspeed:
                self.currentspeed = self.maxspeed
        elif float(accelerate) < 0:
            self.currentspeed += accelerate
            if self.currentspeed < 0:
                self.currentspeed = 0
        else:
            pass
    def move(self, hour):
        self.travelleddistance += self.currentspeed * hour
    def __str__(self):
        return f"{self.name}"

class Electrical(Auto):
    def __init__(self, name, platenumber, maxspeed, capacity):
        super().__init__(name, platenumber, maxspeed)
        self.capacity = capacity

class Gasoline(Auto):
    def __init__(self, name, platenumber, maxspeed, volume):
        super().__init__(name, platenumber, maxspeed)
        self.volume = volume

sakke = Electrical('Sakke', "ABC-15", 180, 52.5)
munttu = Gasoline('Munttu', "ACD-123", 165, 32.3)

time = 0

while time <= 3:
    sakke.accele(random.randint(0,200))
    munttu.accele(random.randint(9,11))
    sakke.move(1)
    munttu.move(1)
    time += 1
print(sakke.travelleddistance)
print(munttu.travelleddistance)