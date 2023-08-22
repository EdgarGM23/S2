import os
os.system("cls")

cadena = input("Ingrese la cadena: ")
inverso = ""

for caracter in cadena:
    inverso = caracter + inverso
print(inverso)