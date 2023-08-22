import os
os.system("cls")

base = int(input("Base: "))
potencia = int(input("Potecia: "))

resultado = 1

for i in range(1, potencia+1):
    resultado *= base
print(f"Resultado = {resultado}")