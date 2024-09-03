#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random
luku = int(input("Anna heitettävien arpakuutioiden määrä: "))
maara = 1
numbers = []
tulos = 0
while luku >= maara:
    number = random.randint(1, 6)
    numbers.append(number)
    maara = maara + 1
for number in numbers:
    tulos = tulos + number
print(numbers)
print(tulos)