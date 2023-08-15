import os
os.system("cls")

unidades = int(input("Unidades: "))

if unidades in range(1,26): precio = 27
elif unidades in range(26,51): precio = 25
elif unidades >= 51: precio = 23 

compra = unidades * precio
descuento = 0.05 * compra

if unidades > 50: descuento = 0.15 * compra

total = compra - descuento

print("El importe de la compra es: ", compra," soles")
print("El descuento es: ", descuento," soles")
print("El total es: ", total," soles")