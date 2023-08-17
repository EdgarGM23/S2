import os
os.system("cls")

angulo = int(input("Ingrese el angulo: "))

if angulo == 0: print("El angulo es nulo")
elif angulo > 0 and angulo < 90: print("El angulo es agudo")
elif angulo == 90: print("El angulo es recto")
elif angulo > 90 and angulo < 180: print("El angulo es obtuso")
elif angulo == 180: print("El angulo es llano")
elif angulo > 180 and angulo < 360: print("El angulo es concavo")
elif angulo == 360: print("El angulo es completo")
else: print(" El angulo no existe")