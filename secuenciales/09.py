import os
os.system("cls")

numeroE = int(input("Ingrese el numero: "))
suma = 0

while numeroE>0:
    suma += (numeroE % 10)
    numeroE = numeroE // 10
print(f"La suma de las cifras es: {suma}")