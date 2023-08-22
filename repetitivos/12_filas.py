import os
os.system("cls")

contador = 0
numeros = ""

for i in range(1, 101):
    contador += 1
    numeros += str(i) + ("\n" if contador%10==0 else ", ")

print(numeros)