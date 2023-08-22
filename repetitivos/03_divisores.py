import os
os.system("cls")

numero = int(input("Numero entero: "))

divisores = 0
fila = ""

for i in range(1, numero+1):
    if numero % i == 0:
        fila += str(i) + (", " if i < numero else "")
print(f"Los divisores son: {fila}")