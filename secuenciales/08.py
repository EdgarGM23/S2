import os
os.system("cls")
import math

radio=int(input("Ingrese la radio: "))
altura=int(input("Ingrese la altura: "))

areabase=math.pi*radio*radio
arealateral=2*math.pi*radio*altura
areatotal=2*areabase*arealateral

print(f"El area base del cilindro es: {format(areabase,'.2f')}")
print(f"El area lateral del cilindro es: {format(arealateral,'.2f')}")
print(f"El area total del cilindro es: {format(areatotal,'.2f')}")