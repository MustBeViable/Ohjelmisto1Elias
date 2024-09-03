#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta
# nimienkysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi
# kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja
# for/in toistorakennetta niiden läpikäymiseen.
names = []
for name in range (5):
    nam = input("Anna: ")
    if not nam:
        break
    names.append(nam)
for name in names:
    print(name)