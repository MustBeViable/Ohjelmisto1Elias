#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen
# summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
# palauttaman summan.
def summa(sum):
    tulo=0
    for i in sum:
        tulo= tulo + i
    return tulo

summat = [1,2,3,4,5]
print(summa(summat))
summat = [2,3]
print(summa(summat))