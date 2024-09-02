#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen
# mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimi = (input("Anna nimi tai lopeta painamalla enter: "))
nimet = set()
while nimi:
    nimet.add(nimi)
    nimi = (input("Anna nimi tai lopeta painamalla enter: "))
for n in nimet:
    print(n)
