import os
os.system("cls")

monto = float(input("Monto vendido: "))

if monto <= 5000: comision = 0.05
elif monto > 5000 and monto <= 10000: comision = 0.08
elif monto > 10000 and monto <= 20000: comision = 0.1
else: comision = 0.15

sueldo_bruto = 250 + (monto * comision)

if sueldo_bruto > 3500: descuento = 0.15
else: descuento = 0.08

sueldo_neto = sueldo_bruto * (1 - descuento)

print(f"El sueldo bruto es: S/ {sueldo_bruto:.2f}")
print(f"El sueldo neto es: S/ {sueldo_neto:.2f}")
print(f"El descuento es de: S/ {(sueldo_bruto - sueldo_neto):.2f}")
print(f"La comision aplicada es: {(comision * 100):.2f}%")