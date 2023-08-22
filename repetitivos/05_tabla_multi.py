import os
os.system("cls")

numero = int(input("Numero: "))

for i in range(1, 12+1):
    resultado = numero * i
    print(f"{numero}*{i} = {resultado}")