import os
os.system("cls")

metros=int(input("Ingrese el valor: "))

centimetros=metros*100
pulgadas=centimetros/2.56
pie=pulgadas/12
yarda=pie/3

print("El valor de ",metros," en centimetros es: ", centimetros)
print("El valor de ",metros," en pulgadas es: ", round(pulgadas,2))
print("El valor de ",metros," en pies es: ", round(pie,2))
print("El valor de ",metros," en yardas es: ", round(yarda,2))