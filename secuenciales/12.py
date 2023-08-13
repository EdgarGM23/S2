import os, math
os.system("cls")
from math import sqrt

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

if (b*b-(4*a*c))<0:
    print("Esta operacion no se puede realizar, intente con otros numeros")
else:
    Solucion1 = (-b-sqrt(b*b-(4*a*c)))/(2*a)
    Solucion2 = (-b+sqrt(b*b-(4*a*c)))/(2*a)

    print("Las solucinoses son: ",Solucion1,"y", Solucion2)