import os
os.system("cls")

numero = int(input("Numero: "))

if numero%2!=0 and numero%3!=0 and numero%5!=0:
    print("El numero es primo")
elif numero==2 or numero==3 or numero==5: print("El numero es primo")
else: print("El numero no es primo")