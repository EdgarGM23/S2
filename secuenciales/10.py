import os
os.system("cls")

numeroE = int(input("Ingrese el numero: "))

cifra1 = numeroE % 10
cifra2 = (numeroE // 10)%10
cifra3 = (numeroE // 100)%10
cifra4 = (numeroE // 1000)%10

print(cifra1, cifra2, cifra3, cifra4)