import os
os.system("cls")
from math import sqrt

catetoA = int(input("Ingrese el cateto adyasente: "))
catetoO = int(input("Ingrese el cateto opuesto: "))

hipotenusa = sqrt(catetoA**2 + catetoO**2)

print("La hipotenusa es: ", hipotenusa)