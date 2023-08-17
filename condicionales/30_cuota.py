import os
os.system("cls")

cuota = int(input("Cuota: "))
dia = int(input("Dia: "))

if dia <=10: 
    if 5 < (cuota * 0.02): descuento = 0.02
    else: descuento = 5
    total = cuota - (cuota * descuento)
elif dia <= 20 and dia > 10:
    descuento = 0
    total = cuota - (cuota * descuento)
else: 
    if 10 < (cuota * 0.03): aumento = 0.03
    else: aumento = 10
    total = cuota + (cuota * aumento)

print(f"El valor a pagar es: S/ {total}")
if total >= cuota: print(f"El recargo es de: S/ {total - cuota}")
else: print(f"El descuento es de: S/ {cuota - total}")