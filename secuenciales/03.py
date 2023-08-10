import os
os.system("cls")

parte1=int(input("Ingrese la primera parte recorrida en kilometros: "))
parte2=int(input("Ingrese la segunda parte recorrida en pies: "))
parte3=int(input("Ingrese la tercera parte recorrida en millas: "))

metro1=parte1*1000
metro2=parte2/3.2808
metro3=parte3/1609

recorridoMetro=metro1+metro2+metro3

yarda1=parte1*1093.61
yarda2=parte2/3
yarda3=parte3*1760

recorridoYarda=yarda1+yarda2+yarda3

print("-----------------------------------------------------------------\n")

print("El recorrido total en metros es: ",round(recorridoMetro,2))
print("El recorrido total en yardas es: ",round(recorridoYarda,2))