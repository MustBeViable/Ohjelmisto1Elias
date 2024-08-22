import random
num1 = int(input("Arvaa luku: "))
num2 = int(9)
#num2 = random.randint(1,10)
while num1 != num2:
    if int(num1) < int(num2):
        print("Liian pieni arvaus.")
        num1 = int(input("Arvaa luku: "))
        #print("t1")
    if float(num1) > float(num1):
        print("Liian suuri arvaus.")
        num1 = int(input("Arvaa luku: "))
        #print("t2")
    if int(num1) == int(num2):
        #print("t3")
        print("Oikein.")