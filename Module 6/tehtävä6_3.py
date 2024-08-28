#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
# paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen
# litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
# negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa
def yksikko(freedomunits):
    freehealthcareunits = float(freedomunits) * 3.785
    print(f"Se on {freehealthcareunits} litraa.")
    return
freedomunits = input("Anna gallonamäärä: ")
while freedomunits:
    if float(freedomunits) >= 0:
        yksikko(freedomunits)
        freedomunits = input("Anna gallonamäärä: ")
    else:
        break