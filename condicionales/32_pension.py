import os
os.system("cls")

promedio = float(input("Promedio: "))
categoria = input("Categoria: ")

descuento = 0
pension = 0

if promedio >= 14 and promedio < 16: descuento = 0.1
elif promedio >= 16 and promedio < 18: descuento = 0.12
elif promedio >= 18 and promedio <= 20: descuento = 0.15
else: print("El promedio no es valido")

if categoria == "A": pension = 550
elif categoria == "B": pension = 500
elif categoria == "C": pension = 450
elif categoria == "D": pension = 400
else: print("La categoria no es valida")

total = pension - (pension * descuento)

print(f"La pension es:          S/{pension}")
print(f"El descuento es:        {descuento*100}%")
print(f"La nueva pension es:    S/{total}")