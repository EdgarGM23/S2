import os
os.system("cls")

Pproducto = int(input("Ingrese el precio del producto: "))
Cproducto = int(input("Ingrese la cantidad del producto: "))

DescProducto = Pproducto*15/100
SegundoDesc = (Pproducto - DescProducto)*15/100

ImporteCom = Pproducto * Cproducto
ImportePagar = (Pproducto - (DescProducto + SegundoDesc)) * Cproducto
Descuento = ImporteCom - ImportePagar

print("El importe de la compra es: ",ImporteCom,"soles")
print("El descuento es de: ",round(Descuento,2),"soles")
print("El importe a pagar es: ",ImportePagar,"soles")

print(SegundoDesc)