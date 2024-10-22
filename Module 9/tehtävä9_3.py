#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua
#matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion
#tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan
#lukemaan 2090 km.

class Auto:
    def __init__(self, PlateNumber, MaxSpeed):
        self.PlateNumber = PlateNumber
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = 60
        self.TravelledDistance = 2000
    def accele(self, Accelerate):
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
    def move(self, hour):
        self.TravelledDistance += self.CurrentSpeed * hour
ferrari = Auto("ABC-123", 200)
ferrari.move(1.5)
print(ferrari.TravelledDistance)