import os
os.system("cls")

monto = float(input("Monto: "))

contador = 0

if monto > 5000:
    sub = monto - 5000
    while sub >= 500:
        sub -= 500
        contador += 1
    extra = monto * 0.1
    sueldo = extra + (25 * contador)
else: sueldo = monto * 0.1

print(f"EL sueldo del vendedor es: S/{sueldo:.2f}")