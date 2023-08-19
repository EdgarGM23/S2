import os
os.system("cls")

edad1 = int(input("Edad 1: "))
edad2 = int(input("Edad 2: "))
edad3 = int(input("Edad 3: "))

if edad1 > edad2 and edad1 > edad3: mayor = edad1
elif edad2 > edad1 and edad2 > edad3: mayor = edad2
elif edad3 > edad1 and edad3 > edad2: mayor = edad3

if edad1 < edad2 and edad1 < edad3: menor = edad1
elif edad2 < edad1 and edad2 < edad3: menor = edad2
elif edad3 < edad1 and edad3 < edad2: menor = edad3

print(f"La mayor edad es: {mayor}")
print(f"La menor edad es: {menor}")
