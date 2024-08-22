import random
num1 = int(input("Arvaa numero: "))
num2 = random.randint(1,10)
while num1 != num2:
    if num1 < num2:
        print("Liia pieni")
        num1 = int(input("Arvaa numero: "))
    elif num1 > num2:
        print("liia iso")
        num1 = int(input("Arvaa numero: "))
else:
    print("oikein")