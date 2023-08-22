import os
os.system("cls")

numero = int(input("Factorial del numero: "))

resultado = 1
final = 1

for i in range(1, numero+1):
    resultado *= i
print(resultado)