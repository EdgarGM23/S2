import os, numpy as np
os.system("cls")

numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))
numero3 = int(input("Tercer numero: "))
numero4 = int(input("Cuarto numero: "))
numero5 = int(input("Quinto numero: "))

numeros = [numero1, numero2, numero3, numero4, numero5]

numeros.sort(reverse=True)

numero1 = numeros[0]
numero2 = numeros[1]
numero3 = numeros[2]

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los 3 numeros mayores es: {promedio:.2f}")