num = input("Anna numero: ")
if not num:
    print("t1")
else:
    float(num)
    print("t2")
nummax = num
nummin = num
print("t3")
while num:
    print("t4")
    if float(num) > float(nummax):
        nummax = num
        print("t5")
    elif float(num) < float(nummin):
        nummin = num
        print("t6")
    print("t7")
    num = input("Anna numero: ")
    if not num:
        print(f"Pienin numero on {nummin} ja suurin numero on {nummax}")
        print("testi vika")