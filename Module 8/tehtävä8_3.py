import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='eliasellu',
         password='Koira123',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
# etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys
# geopy-kirjaston avulla
def cordinate(code):
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{code}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
#    print(result)
    return result
#    print(type(result))
#    print(f"{result[0][0]}, {result[0][1]}")
ICAO1 = input("A: ")
#cordinate(ICAO1)
ICAO2 = input("B: ")
#cordinate(ICAO2)
airport1 = cordinate(ICAO1)
airport2 = cordinate(ICAO2)
dist = distance.distance(airport1, airport2).km
print(f"Lentokenttien etäisyys on {dist:.2f} km.")