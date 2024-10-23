#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.




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
        self.elevators = []
        self.highest = highest
        self.lowest = lowest
        self.elevator_count = elevator_count
        for i in range(elevator_count):
            elevator = Elevator(lowest, highest)
            self.elevators.append(elevator)

    def drive_elevators(self, elevator_number, floor):
        print(f"Hissi {elevator_number} lähtee liikkeelle!")
        self.elevators[elevator_number-1].move_to(floor)

    def fire_alarm(self):
        print("Tulipalo")
        for elevator in range(len(self.elevators)):
            print(f"Hissi {elevator+1} lähtee liikkeelle!")
            self.elevators[elevator].move_to(self.lowest)
        print("Palotuli")

house = Building(1, 10, 2)
house.drive_elevators(1, 5)
house.drive_elevators(2, 6)
house.fire_alarm()