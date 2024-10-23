#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän
# kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista
# tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja
#kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Elevator:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.floor = self.lowest
    def move_to(self, floor):
        while floor < self.floor:
            self.move_down()
        while floor > self.floor:
            self.move_up()
        else:
            print(f"Hissi on kerroksessa {self.floor}")

    def move_up(self):
        if self.floor >= self.highest:
            self.floor = self.highest
            print(f"Hissi on kerroksessa {self.floor}")
        else:
            print(f"Hissi on kerroksessa {self.floor}")
            self.floor += 1

    def move_down(self):
        if self.floor <= self.lowest:
            self.floor = self.lowest
            print(f"Hissi on kerroksessa {self.floor}")
        else:
            print(f"Hissi on kerroksessa {self.floor}")
            self.floor -= 1

class Building:
    def __init__(self, lowest, highest, elevator_count):
        self.elevator = []
        self.highest = highest
        self.lowest = lowest
        self.elevator_count = elevator_count
        for i in range(elevator_count):
            elevator = Elevator(lowest, highest)
            self.elevator.append(elevator)

    def drive_elevators(self, elevator_number, floor):
        print(f"Hissi {elevator_number} lähtee liikkeelle")
        Elevator.move_to(self.elevator[elevator_number-1], floor)
house = Building(1, 10, 2)
house.drive_elevators(1, 5)
house.drive_elevators(2, 6)