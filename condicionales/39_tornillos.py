import os
os.system("cls")

horas = float(input("Horas ausentes: "))
Tdefectuosos = int(input("Tornillos defectuosos: "))
tornillos = int(input("Tornillos no defectuosos: "))

categoria1 = 0
categoria2 = 0
categoria3 = 0

if horas < 1.5: categoria1 = 1
if Tdefectuosos < 300: categoria2 = 1
if tornillos > 10000: categoria3 = 1

print("------------------------------------")

if categoria1 == 0 and categoria2 == 0 and categoria3 == 0: print("El grado del trabajador es 5")
elif categoria1 == 1 and categoria2 == 0 and categoria3 == 0: print("El grado del trabajador es 7")
elif categoria1 == 0 and categoria3 == 0 and categoria2 == 1: print("El grado del trabajador es 8")
elif categoria1 == 0 and categoria2 == 0 and categoria3 == 1: print("El grado del trabajador es 9")
elif categoria1 == 1 and categoria2 == 1 and categoria3 == 0: print("El grado del trabajador es 12")
elif categoria1 == 1 and categoria3 == 1 and categoria2 == 0: print("El grado del trabajador es 13")
elif categoria2 == 1 and categoria3 == 1 and categoria1 == 0: print("El grado del trabajador es 15")
elif categoria1 == 1 and categoria2 == 1 and categoria3 == 1: print("El grado del trabajador es 20")