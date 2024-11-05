import mysql.connector
from flask import Flask, request

yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='kolovastaava',
         password='kolovastaava',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

app = Flask(__name__)
@app.route('/airport_info')
def airport_info():
    args = request.args
    icao = args['icao']
    sql = (f" SELECT ident as ICAO, name as Name, municipality as Municipality"
           f" FROM airport WHERE ident = '{icao}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result[0])
    print(f"Lentokentän {result[0]['Name']} tiedot:\nICAO: {result[0]['ICAO']}\nKaupunki: {result[0]['Municipality']}.")
    return result[0]

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)