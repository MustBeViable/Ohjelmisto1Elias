import random
num1 = int(input("Arvaa luku: "))
num2 = int(10)
#num2 = random.randint(1,10)
while num1 != num2:
    if num2 < num1:
        print("Liian pieni arvaus.")
        num1 = int(input("Arvaa luku: "))
        print("t1")
    elif num2 > num1:
        print("Liian suuri arvaus.")
        num1 = int(input("Arvaa luku: "))
        print("t2")
    elif num1 == num2:
        print("t3")
        print("Oikein.")