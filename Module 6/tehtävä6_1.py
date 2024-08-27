#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita
#pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun
# silmäluvun.
import random
def noppa():
    num1 = random.randint(1,6)
    return num1
num2 = noppa()
while num2 != 6:
    print(f"Saatu silmäluku on {num2}.")
    num2 = noppa()