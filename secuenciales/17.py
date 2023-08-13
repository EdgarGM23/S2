import os
os.system("cls")

donacion = int(input("Ingrese el monto de la donacion: "))

Csalud = donacion*25/100
Cinfantil = donacion*35/100
Einfantil = donacion*25/100
Aancianos = donacion - Csalud - Cinfantil -Einfantil

print("Los montos asignados son: ")
print("Centro de salud: ", Csalud,"soles")
print("Comedor infantil: ", Cinfantil,"soles")
print("Escuela infantil: ", Einfantil,"soles")
print("Asilo de ancianos: ", Aancianos,"soles")