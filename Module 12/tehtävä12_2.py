

# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan
# Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua
# Celsius-asteiksi. Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
# tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

city_name = input("Anna kaupunki, jonka sään haluat tietää: ").capitalize()
api_key = "ec2ab774c34c8f15bb4dffa8379729d3"
try:
    req = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    answer = requests.get(req).json()
    print(answer[0]["lat"], answer[0]["lon"])
    latitude = answer[0]["lat"]
    longitude = answer[0]["lon"]
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
try:
    req2 = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    answer2 = requests.get(req2).json()
    weather = answer2["weather"][0]["description"]
    degrees = answer2["main"]["temp"] - 273.15
    print(f"Kaupunissa {city_name} on nyt {weather} ja"
          f"{degrees: .2f} Celsius astetta lämmintä.")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
