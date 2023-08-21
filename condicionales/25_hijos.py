import os
os.system("cls")

sueldo = float(input("Sueldo bruto: "))
hijos = int(input("Numero de hijos: "))

bono = 1

if hijos > 1: 
    bonificacion = sueldo * 0.125
    contador = hijos
    while contador > 0:
        contador -= 1
        bono +=1
    extra = 40 * (bono - 1)
else: 
    bonificacion = sueldo * 0.1
    extra = 40

sueldo_neto = sueldo + bonificacion + extra

print(f"La bonificacion es de:      S/{bonificacion}")
print(f"El sueldo total es de:      S/{sueldo_neto}")