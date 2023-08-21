import os
os.system("cls")

numero1 = int(input("Numero1: "))
numero2 = int(input("Numero2: "))
numero3 = int(input("Numero3: "))

if numero1 > numero2 and numero2 > numero3: print(f"Los numero fueron agregados de forma descendente")
elif numero1 < numero2 and numero2 < numero3: print(f"Los numero fueron agregados de forma ascendente")
else: print(f"Los numeros fueron agregados en desorden")