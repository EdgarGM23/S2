import os
os.system("cls")

docenas = int(input("Docenas: "))
precio = int(input("Precio: "))

if docenas >= 6: descuento = 0.15
else: descuento = 0.1

if docenas >= 30:
    lapiceros = docenas // 3
else: lapiceros = 0

total = (docenas * precio) * (1-descuento)

print(f"El monto de la compra es: S/ {docenas * precio}")
print(f"El descuento es : S/ {descuento}")
print(f"El total a pagar es: S/ {total}")
print(f"Los lapiceros a regalar son: {lapiceros}")