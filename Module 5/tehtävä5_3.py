#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
num = int(input("Enter a number: "))
if num > 1:
    print("t0")
    if num != 2 or num != 3:
        print("t1")
        for i in range(2, int((num//2)+1)):
            print("t2")
            if num % i == 0:
                print("t3")
                print("Ei alkuluku")
                break
            else:
                print("t4")
                print("Alkuluku")
                break
    else:
        print("t5")
        print("Alkuluku")
else:
    print("t5")
    print("Ei alkuluku")