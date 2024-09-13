import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='eliasellu',
         password='Koira123',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
# lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

def airport(countrycode):
    sql = (f" SELECT type, count(*)"
           f" FROM airport"
           f" where iso_country = '{countrycode}'"
           f" group by type")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result1 = kursori.fetchall()
    print(result1)
    print(type(result1))
    for i in result1:
        print(f"{i[0]}: {i[1]}")

countrycode = input("Give me country code like FI: ")
airport(countrycode)