import os
os.system("cls")

donacion = int(input("Donacion: "))

if donacion >=10000:
    centroS = donacion * 0.3
    centroN = donacion * 0.5
    bolsa = donacion - (centroN + centroS)
else:
    centroS = donacion * 0.25
    centroN = donacion * 0.6
    bolsa = donacion - (centroN + centroS)

print(f"El monto dirigido al Centro de Salud es: S/ {centroS}")
print(f"El monto dirigido al Comedor de Niños es: S/ {centroN}")
print(f"El monto dirigido a la bolsa es: S/ {bolsa}")