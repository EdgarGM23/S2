import os
os.system("cls")

vendido = int(input("Ingrese el total vendido: "))

comision = vendido * 9/100
Sbruto = 500 + comision
Sneto = Sbruto - (Sbruto * 11/100)

print("La comision es: ", comision)
print("El sueldo bruto es: ", Sbruto)

if Sneto > 500:
    print("El vendedor tuvo un aumento de: ",round(Sneto-500,2))
elif Sneto == 500:
    print("El vendedor no tuvo aumento ni descuento")
else:
    print("El vendedor tuvo un descuento de: ",round(500-Sneto,2))

print("El sueldo neto es: ", Sneto)