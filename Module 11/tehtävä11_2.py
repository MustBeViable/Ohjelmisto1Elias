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
        self.max_speed = maxspeed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, accelerate):
        if float(accelerate) > 0:
            self.current_speed += accelerate
            if self.current_speed >= self.max_speed:
                self.current_speed = self.max_speed
        elif float(accelerate) < 0:
            self.current_speed += accelerate
            if self.current_speed < 0:
                self.current_speed = 0
        else:
            pass

    def move(self, hour):
        self.travelled_distance += self.current_speed * hour

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
    sakke.accelerate(random.randint(0, 200))
    munttu.accelerate(random.randint(9, 11))
    sakke.move(1)
    munttu.move(1)
    time += 1
print(f"{sakke.name} on liikkunut {sakke.travelled_distance} km.")
print(f"{munttu.name} on liikkunut {munttu.travelled_distance} km.")