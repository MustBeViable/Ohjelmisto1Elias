num1 = input("Enter number: ")
if not num1:
    print("t1")
else:
    float(num1)
nummin  = num1
nummax = num1
#    num1 = float(input("Enter number: "))
while num1:
    if num1 > nummax:
        nummax = num1
        print("1")
    elif num1 < nummin:
        nummin = num1
        print("2")
    num1 = input("Enter number: ")
    if not num1:
        print("3")
        print(f"pienin {nummax} ja suurin {nummax}")
        break
    else:
        float(num1)
        print("4")