import os
os.system("cls")

tardanza = int(input("Tardanza en minutos: "))
rendimiento = int(input("Numero de observaciones: "))

if tardanza > 9: puntajeT = 0
elif tardanza in range(6, 10): puntajeT = 4
elif tardanza in range(3, 6): puntajeT = 6
elif tardanza in range(1, 3): puntajeT = 8
else: puntajeT = 10

if rendimiento > 3: puntajeR = 0
elif rendimiento == 3: puntajeR = 1
elif rendimiento == 2: puntajeR = 5
elif rendimiento == 1: puntajeR = 8
else: puntajeR = 10

total = puntajeR + puntajeT

if total < 11: bonificacion = 2.5
elif total in range(11, 14): bonificacion = 5
elif total in range(14, 17): bonificacion = 7.5
elif total in range(17, 20): bonificacion = 10
else: bonificacion = 12.5

print(f"El puntaje del empleado es:         {total}")
print(f"La bonificacion del empleado es:    {bonificacion}")