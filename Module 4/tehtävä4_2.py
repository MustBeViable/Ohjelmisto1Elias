inch = float(input("Anna tuumamäärä: "))
while inch > 0:
    print(inch*2.54)
    inch = float(input("Anna tuumamäärä: "))
    if inch < 0:
        break