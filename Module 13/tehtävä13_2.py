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
@app.route('/')
