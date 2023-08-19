import os
os.system("cls")

examen1 = float(input("Examen 1: "))
examen2 = float(input("Examen 2: "))
examen3 = float(input("Examen 3: "))

propina = 20

if examen1 > 10: propina += 5
if examen2 > 10: propina += 5
if examen3 > 10: propina += 5

print(f"La propina que recibira es: {propina}")
