import random
kerta = int(input("Anna pisteiden lukumäärä: "))
maara = 0
inside = 0
outside = 0
while maara < kerta:
    CORX=random.uniform(-1,1)
    CORY=random.uniform(-1,1)
    maara = maara + 1
    outside = outside + 1
    if CORX**2+CORY**2<1:
        inside = inside + 1
if outside == 0:
    outside = outside + 1
print((4*inside)/outside)