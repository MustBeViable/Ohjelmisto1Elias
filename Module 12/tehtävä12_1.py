#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
# esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import json

want_joke = input("Haluatko kuulla vitsin (y/n): ").lower()

while want_joke == "y":
    try:
        req = "https://api.chucknorris.io/jokes/random"
        answer = requests.get(req).json()
        print(answer["value"])
    except requests.exceptions.RequestException as e:
        print("Hakua ei voitu suorittaa.")
    want_joke = input("Haluatko kuulla vitsin (y/n): ").lower()
