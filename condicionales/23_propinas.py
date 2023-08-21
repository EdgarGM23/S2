import os
os.system("cls")

matematica = int(input("Nota de Matematica: "))
fisica = int(input("Nota de Fisica: "))

if matematica > 17: mat_propina = matematica + 3
else: mat_propina = matematica

if fisica > 15: fis_propina = (fisica * 0.5) + 2
else: fis_propina = fisica * 0.5

promedio = (matematica + fisica)/2

print(f"La propina por los examenes de matematica es:   S/{mat_propina}")
print(f"La propina por los examenes de fisica es:       S/{fis_propina}")
print(f"La propina total es:                            S/{mat_propina + fis_propina}")

if promedio > 16: print(f"Obtiene un reloj con un promedio de {promedio}")
else: print(f"No obtiene un rejol por obtener el promedio de: {promedio}")