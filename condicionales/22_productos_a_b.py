import os
os.system("cls")

A = int(input("Unidades del producto A: "))
B = int(input("Unidades del producto B: "))

if A > 50: descuento_A = 0.15
else: descuento = 0
if B > 60: descuento_B = 0.1
else: descuento = 0

costo_A = A * 25
costo_B = B * 30

total_A = costo_A * (1 - descuento_A)
total_B = costo_B * (1 - descuento_B)

total_final = total_A + total_B
dst_A = costo_A - total_A
dst_B = costo_B - total_B
dst_final = dst_A + dst_B

print(f"El importe bruto del producto A es de:  S/{costo_A}")
print(f"El importe bruto del producto B es de:  S/{costo_B}")
print(f"El descuento del producto A es de:      S/{dst_A}")
print(f"El descuento del producto B es de:      S/{dst_B}")
print(f"El descuento final es de:               S/{dst_final}")
print(f"El total final a pagar es:              S/{total_final}")

