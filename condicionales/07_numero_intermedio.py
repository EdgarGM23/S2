import os
os.system("cls")

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

orden = [numero1, numero2, numero3]

orden.sort()

print(f"El numero intermedio es {orden[1]}")