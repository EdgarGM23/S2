import os
os.system("cls")

numero = int(input("Numero entero: "))

contador = 0
divisores = 0
fila = ""

for i in range(1, numero+1):
    if numero % i == 0:
        fila += str(i) + (", " if i < numero else "")
        contador += 1
print(f"Los divisores son: {fila}")
print(f"La cantidad de divisores es: {contador}")