#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.


"""alla poistettu koodipätkä mikä vie hissit aina alas. Vähän turha, jos palohälytys tekee tuon"""
"""        while self.floor != self.lowest:
            if floor > self.lowest:
                self.move_down()"""

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
        Elevator.move_to(self.elevator[elevator_number-1], floor)
    def fire_alarm(self):
        for i in range(len(self.elevator)):
            Elevator.move_to(self.elevator[i], self.lowest)
house = Building(1, 10, 2)
house.drive_elevators(1, 5)
house.drive_elevators(2, 6)
house.fire_alarm()