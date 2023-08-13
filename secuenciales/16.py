import os
os.system("cls")

tarifa = int(input("Ingrese la tarifa horaria: "))
horas = int(input("Ingrese las horas de trabajo: "))

Sbase = tarifa * horas
Sbruto = Sbase + (Sbase*20/100)
Sneto = Sbruto - (Sbruto*10/100)

print("--------------------------------------------")

print("El sueldo base es: ", Sbase)
print("El sueldo bruto es: ", Sbruto)
print("El sueldo neto es: ", Sneto)