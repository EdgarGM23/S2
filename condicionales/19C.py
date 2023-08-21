import os
os.system("cls")

sexo = input("Sexo: ")
edad = int(input("Edad: "))

categoria = "No definida"

if sexo == "femenino" and edad < 23:
    categoria = "FA"
elif sexo == "femenino" and edad >= 23:
    categoria = "FB"
else: print("Los valores ingresados no son validos")

if sexo == "masculino" and edad < 25:
    categoria = "FA"
elif sexo == "masculino" and edad >= 25:
    categoria = "FB"
else: print("Los valores ingresados no son validos")

print(f"La categoria es: {categoria}")