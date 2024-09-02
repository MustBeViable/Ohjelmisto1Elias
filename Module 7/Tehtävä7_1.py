#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
# vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

vaika=("kevät", "kesä", "syksy", "talvi")
num = int(input("Anna kuukauden numero: "))
if num >= 3 and num <= 5:
    print(vaika[0])
elif num >= 6 and num <= 8:
    print(vaika[1])
elif num >= 9 and num <= 11:
    print(vaika[2])
else:
    print(vaika[3])