import os
os.system("cls")

base=int(input("Ingrese la base: "))
altura=int(input("Ingrese la altura: "))

area=base*altura
perimetro=(base+altura)*2

print(f"El area del rectangulo es: {format(area,'.2f')}")
print(f"El perimetro del rectangulo es: {format(perimetro,'.2f')}")