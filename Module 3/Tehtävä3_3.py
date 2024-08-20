gender = input("Anna sukupuolesi (pienellä): ")
blood = float(input("Anna hemoglobiiniarvosi: "))
if gender == "nainen" and blood < 117:
    print("Hemoglobiiniarvosi on alhainen")
elif gender == "nainen" and blood > 175:
    print("Hemoglobiiniarvosi on korkea")
elif gender == "nainen" and blood <= 175 and blood >= 117:
    print("Hemoglobiiniarvosi on normaali.")
elif gender == "mies" and blood <= 134 and blood >= 195:
    print("Hemoglobiiniarvosi on normaali.")
elif gender == "mies" and blood < 134:
    print("Hemoglobiiniarvosi on alhainen.")
elif gender == "mies" and blood > 195:
    print("Hemoglobiiniarvosi on korkea.")