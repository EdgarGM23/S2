import os
os.system("cls")

numero = int(input("Numero entero: "))

divisores = 0

for i in range(1, numero+1):
    if numero % i == 0:print(i)