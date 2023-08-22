import os
os.system("cls")

multiplos = int(input("Cantidad de multiplos: "))
numero = int(input("Numero: "))

for i in range(1, multiplos+1):
    resultado = numero * i
    print(resultado)