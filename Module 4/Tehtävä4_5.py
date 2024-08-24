#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

tunnus1 = str("python")
salasana1 = str("rules")
tunnus2 = input("Anna käyttäjätunnus: ")
salasana2 = input("Anna salasana: ")
kerta = 0
while tunnus1 != tunnus2 and salasana1 != salasana2 or tunnus1 != tunnus2 or salasana1 != salasana2:
    print("Väärin")
    tunnus2 = input("Anna käyttäjätunnus: ")
    salasana2 = input("Anna salasana: ")
    kerta = kerta + 1
    if kerta >= 5:
        print("Pääsy evätty!")
        break
else:
    print("Tervetuloa")