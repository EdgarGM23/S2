import os
os.system("cls")

monto = float(input("Monto del total vendido: "))

sueldo_bruto = 600 + (monto * 0.15)

if sueldo_bruto > 1800: descuento = 0.1
else: descuento = 0.05
if monto > 1000: polos = 3
else: polos = 1

sueldo_neto = sueldo_bruto * (1 - descuento)
dst = sueldo_bruto - sueldo_neto

print(f"El sueldo bruto es:     S/{sueldo_bruto:.2f}")
print(f"El descuento es de:     S/{dst:.2f}")
print(f"El sueldo neto es:      S/{sueldo_neto:.2f}")
print(f"Los polos regalados son:   {polos}")