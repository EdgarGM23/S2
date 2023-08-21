import os
os.system("cls")

numero = int(input("Numero: "))

cifra1= numero // 100
cifra2= (numero // 10) % 10
cifra3= (numero % 100) % 10

if numero%2 == 0: 
    print("El numero es entero")
    if cifra1 == cifra2 + 1 and cifra2 == cifra3 + 1:
        print("El numero es consecutivo de forma descendente")
    elif cifra2 == cifra1 + 1 and cifra3 == cifra2 + 1 :
        print("El numero es consecutivo de forma ascendente")
    else: print("El numero no es consecutivo")
else: print("El numero ingresado no es entero")