import os
os.system("cls")

codigo = int(input("Codigo: "))
unidades = int(input("Unidades: "))

if codigo == 101: precioU = 17
elif codigo == 102: precioU = 25
elif codigo == 103: precioU = 16
elif codigo == 104: precioU = 27

if unidades >= 1 and unidades <=10: descuento = 0.05
elif unidades >= 11 and unidades <=20: descuento = 0.08
elif unidades >= 21 and unidades <=30: descuento = 0.1
elif unidades >= 31: descuento = 0.13

importe = precioU * unidades
total = importe * (1 - descuento)
dst = importe - total

print(f"El importe de la compra es:     S/{importe}")
print(f"El descuento es:                S/{dst}")
print(f"El total a pagar es:            S/{total}")