import os
os.system("cls")

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

resultado = 0

while numero2 >= 1:
    resultado += numero1
    numero2 -= 1

print(f"El resultado es: {resultado}")