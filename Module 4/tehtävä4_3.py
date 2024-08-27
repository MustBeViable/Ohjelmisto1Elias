num = input("Anna numero: ")
if not num:
    print("Ei ole suurinta eikä pienintä lukua.")
else:
    float(num)
nummax = num
nummin = num
while num:
    if float(num) > float(nummax):
        nummax = num
    elif float(num) < float(nummin):
        nummin = num
    num = input("Anna numero: ")
    if not num:
        print(f"Pienin numero on {nummin} ja suurin numero on {nummax}")