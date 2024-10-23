#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
# alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
# julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Publish:
    def __init__(self, name):
        self.name = name

class Book(Publish):
    def __init__(self, name, page_count, author):
        self.page_count = page_count
        self.author = author
        super().__init__(name)
    def print_info(self):
        print(self.name, self.page_count, self.author)


class Magazine(Publish):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    def print_info(self):
        print(self.name, self.editor)

aku = Magazine("Aku Ankka", "Aki Hyyppä")
hytti = Book("Hytti n:o 6", 200, "Rosa Liksom")
hytti.print_info()
aku.print_info()