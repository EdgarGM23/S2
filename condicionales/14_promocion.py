import os,random
os.system("cls")

numero = random.randrange(1,200)
compra = int(input("Importe de la compra: "))

if numero >= 100: descuento = 0.15
else: descuento = 0.05

total = compra * (1 - descuento)
dst = compra - total

print(f"El numero es: {numero}")
print(f"El descuento es de: S/{dst}")
print(f"El importe total es de: S/{total}")