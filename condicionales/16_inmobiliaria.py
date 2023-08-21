import os
os.system("cls")

ingreso = float(input("Ingreso del comprador: "))
casa = float(input("Costo de la casa: "))

if ingreso < 1250 : 
    cuota_inicial = casa * 0.15
    cuotas_mensuales = (casa - cuota_inicial) / 120
else: 
    cuota_inicial = casa * 0.3
    cuotas_mensuales = (casa - cuota_inicial) / 75

print(f"La cuota inicial es: S/{cuota_inicial}")
print(f"El monto de la cuota mensual es: S/{cuotas_mensuales:.2f}")