import os
os.system("cls")

numero = int(input("Numero: "))

suma = 0

for i in range(1, numero+1):
    if i%3==0 and i%5!=0:
        suma += i
print(f"La suma de los numeros es: {suma}")