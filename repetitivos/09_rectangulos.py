import os
os.system("cls")

numero = int(input("Numero: "))
j = 0

if numero >= 4:
    while j < numero:
        fila = ""
        for i in range(1, (numero *2)+1):
            fila += str("*")
        print(fila)
        j +=1
else: print("El numero tiene que ser mayor a 4")