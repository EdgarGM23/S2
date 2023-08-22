import os
os.system("cls")

multiplos = int(input("Cantidad de multiplos: "))
numero = int(input("Numero: "))

fila = ""

for i in range(1, multiplos+1):
    resultado = numero * i
    fila += str(resultado) + (", " if i < multiplos else "")
print(f"Los multiplos de {numero} son: {fila}")