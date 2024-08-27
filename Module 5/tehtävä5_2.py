#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True
num = input("Enter a number: ")
nums = []
while num:
    nums.append(int(num))
    num = input("Enter a number: ")
    nums.sort(reverse=True)
for num in range(5):
    print(nums[num])