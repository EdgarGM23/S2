import os
os.system("cls")

numero = int(input("Numero: "))
de = int(input("Del numero: "))
a = int(input("Al numero: "))

for i in range(de, a+1):
    resultado = numero * i
    print(f"{numero}*{i} = {resultado}")