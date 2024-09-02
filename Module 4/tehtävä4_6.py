import random
kerta = int(input("Anna pisteiden lukumäärä: "))
maara = 0
inside = 0
kok = 0
while maara < kerta:
    CORX=random.uniform(-1,1)
    CORY=random.uniform(-1,1)
    maara = maara + 1
    kok = kok + 1
    if CORX**2+CORY**2<1:
        inside = inside + 1
if kok == 0:
    kok = kok + 1
print((4*inside) / kok)
