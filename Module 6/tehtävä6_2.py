#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion
# avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
# jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random
def noppa(maara):
    num1 = random.randint(1,maara)
    return num1
maara = int(input("Anna nopan maksimi luku: "))
num1 = noppa(maara)
while num1 != maara:
    print(f"Saatu silmäluku on {num1}")
    num1 = noppa(maara)