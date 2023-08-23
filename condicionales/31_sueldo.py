import os
os.system("cls")

categoria = input("Categoria del trabajador: ")
horas = int(input("Horas trabajadas: "))

if categoria == "A": tarifa = 21
elif categoria == "B": tarifa = 19.5
elif categoria == "C": tarifa = 17
elif categoria == "D": tarifa = 15.5
else: print("La categoria no existe")

sueldo_bruto = horas * tarifa

if sueldo_bruto > 2500: descuento = 0.2
else: descuento = 0.15

total = sueldo_bruto * (1- descuento)
dst = sueldo_bruto - total

print(f"El sueldo bruto es:     S/{sueldo_bruto}")
print(f"El descuento es de:     S/{dst}")
print(f"El sueldo neto es:      S/{total}")