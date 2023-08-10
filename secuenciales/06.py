import os
os.system("cls")
import math

radio = int(input("Indique el radio: "))
altura = int(input("Indique la altura: "))

area = 2*math.pi*radio*(radio+altura)
volumen = math.pi*radio*radio*altura

print(f"El area del cilindro es: {format(area,'.2f')}")
print(f"El volumen del cilindro es: {format(volumen,'.2f')}")