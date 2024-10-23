# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
# siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
# esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
# kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai
# alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
# ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.


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

    def move_up(self):
        if self.floor >= self.highest:
            self.floor = self.highest
        else:
            self.floor += 1
            print(f"Hissi on kerroksessa {self.floor}")

    def move_down(self):
        if self.floor <= self.lowest:
            self.floor = self.lowest
        else:
            self.floor -= 1
            print(f"Hissi on kerroksessa {self.floor}")

elevator = Elevator(1, 10)
elevator.move_to(6)
elevator.move_to(10)
elevator.move_to(3)
elevator.move_to(1)