#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

# - tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo
# kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

# - tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

# - kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# - Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan
# kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
# toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
# kun kilpailu on päättynyt.

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
class Race:
    def __init__(self, name, length, list_of_cars):
        self.name = name
        self.length = length
        self.list_of_cars = list_of_cars
        for i in range(len(self.list_of_cars)):
            self.list_of_cars[i] = Auto(self.list_of_cars[i], "ABC-" + str(i + 1), random.randint(100, 200))
    def hour_pass(self, hour):
        for y in range(len(self.list_of_cars)):
            Auto.accele(self.list_of_cars[y], random.randint(-15, 10))
        for i in range(len(self.list_of_cars)):
            Auto.move(self.list_of_cars[i],hour)
    def race_situation(self, list_of_cars):
        print("\nTämän hetkinen tilanne:\n")
        list_of_emojis = ["(❁´◡`❁)", "(●'◡'●)", "☆*: .｡. o(≧▽≦)o .｡.:*☆", "╰(*°▽°*)╯", "(┬┬﹏┬┬)", "UwU"]
        list_of_emojis2 = ["😘", "😁", "😛", "😍", "🤩", "🧐", "🫣", "🤠"]
        for i in range(len(list_of_cars)):
            print(f"Auton nimi: {list_of_cars[i]}.  Auton rekisterinumero {list_of_cars[i].platenumber} | Auton nopeus: "
                  f"{list_of_cars[i].currentspeed:4.0f} | Auton kulkema matka {list_of_cars[i].travelleddistance:4.0f}\n")
        print('"Yleisö hurraa"\n')
        for i in range(10):
            print(list_of_emojis[random.randint(0, len(list_of_emojis) - 1)], end=" ")
        print("")
        for i in range(30):
            print(list_of_emojis2[random.randint(0, len(list_of_emojis2) - 1)], end=" ")
        print("")
    def race_status(self, list_of_cars, length):
        for i in range(len(list_of_cars)):
            if length <= list_of_cars[i].travelleddistance:
                race_over = True
                return race_over

cars = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7", "auto8", "auto9", "auto10"]
race_length = 8000
race = Race("Suuri romuralli", race_length, cars)
pass_time = 0
while True:
    race.hour_pass(1)
    pass_time += 1
    if pass_time % 10 == 0:
        race.race_situation(cars)
    race_over = race.race_status(cars, race_length)
    if race_over:
        race.race_situation(cars)
        print(f"\nKisa loppui! Kisassa kesti {pass_time} tuntia.")
        break