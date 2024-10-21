import numpy as np
a = 2.493
b = 0.911
c = 137.7
d = 62.3
print("1.1 osion tehtävän 1 vastaukset:")
print("")
print(f"a) {np.degrees(a)} astetta")
print(f"b) {np.degrees(b)} astetta")
print("")
print("1.1 osion tehtävän 2 vastaukset:")
print("")
print(f"a) {np.radians(c)} radiaania")
print(f"b) {np.radians(d)} radiaania")
print("")
print("1.1 osion tehtävän 3 vastaukset:")
print("")
lista = np.array([30,45,60,90,135,150,180,270,360])
for i in lista:
    print(f"{np.radians(i)} radiaania")

print("")
print("Osion 2.2.1 Tehtävä 1:n kolmion hypotenuusa lasku:\n")
print(f"{np.hypot(1.6, 2.3)} m")