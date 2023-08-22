import os
os.system("cls")

texto = input("Ingrese el texto: ")

if texto.isupper():
    print(texto.lower())
else: print(texto.upper())