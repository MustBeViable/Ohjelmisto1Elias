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
def cordinate(code):
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{code}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result
ICAO1 = input("Insert first ICAO code: ")
ICAO2 = input("Insert second ICAO code: ")
airport1 = cordinate(ICAO1)
airport2 = cordinate(ICAO2)
dist = distance.distance(airport1, airport2).km
print(f"Lentokenttien etäisyys on {dist:.2f} km.")