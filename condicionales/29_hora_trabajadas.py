import os
os.system("cls")

horas = int(input("Horas trabajadas: "))
tarifa = float(input("Tarifa horaria: "))

if horas > 48:
    sueldo_bruto = (horas * tarifa) * 1.2
else: sueldo_bruto = horas * tarifa

if sueldo_bruto > 1500: descuento = 0.11
else: descuento = 0

sueldo_neto = sueldo_bruto * (1 - descuento)
dst = sueldo_bruto - sueldo_neto
pago_horas = sueldo_neto / horas

print(f"Las horas trabajadas:   {horas}")
print(f"El pago por hora es:    S/{pago_horas:.2f}")
print(f"El sueldo bruto es:     S/{sueldo_bruto:.2f}")
print(f"El descuento es de:     S/{dst:.2f}")
print(f"El total a pagar es:    S/{sueldo_neto:.2f}")