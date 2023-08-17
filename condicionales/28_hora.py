import os
os.system("cls")

hora = int(input("Ingrese la hora: "))

horaplus = [1,2,3,4,5,6,7,8,9,10,11,12]

if hora > 12 and hora < 25:
    print(f"Son las {horaplus[hora-13]}")
elif hora > 24:
    print("Esa hora no es valida")
else: print(f"Son las {hora}")