import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='eliasellu',
         password='Koira123',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
# lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on
# tallennettuna airport-taulun ident-sarakkeeseen.

def town(city):
    sql = (f" SELECT airport.name, municipality"
           f" FROM airport"
           f" WHERE ident = '{city}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    #print(result)
    return result

ICAO1 = input("It would be rather pleasant, if you would give me a ICAO: ")
result1 = []
result1 = town(ICAO1)
#print(result1)
#tuple = result1[0]
    #erotetaan listan uloimmat listat
#name, municipality = tuple
    #muuttaa ylemmän listan arvot ja määrittää ne "name":n ja "municipality":n alle

#print(f"Your given ICAO code ({ICAO1}) belongs to {name} and it is in {municipality}")
#print(f"Your given ICAO code ({ICAO1}) belongs to {tuple[0]} and it is in {tuple[1]}")
print(f"Your given ICAO code ({ICAO1}) belongs to {result1[0][0]} and it is in {result1[0][1]}.\n"
      f"Do whatever you like with this information!")
    #Lista listan sisällä, jolloin eka [] määrittää mistä listatsta uloimmasta päin katsotaan ja toinen [] määrittää
    #sen  sisältä