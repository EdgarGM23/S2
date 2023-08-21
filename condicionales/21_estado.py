import os
os.system("cls")

numero = int(input("Numero: "))

cifra1= numero // 1000
cifra_edad = (numero // 10) % 100
cifra4= (numero%100) % 10

continuar_c1 = True
continuar_c4 = True

if cifra1 == 1: estado = "Soltero"
elif cifra1 == 2: estado = "Casado"
elif cifra1 == 3: estado = "Divorciado"
elif cifra1 == 4: estado = "Viudo"
else: 
    print("El estado civil no existe")
    continuar_c1 = False

if cifra4 == 1: genero = "Masculino"
elif cifra4 == 2: genero = "Femenino"
else: 
    print("El genero no existe")
    continuar_c4 = False

if continuar_c1 and continuar_c4: 
    print(f"El estado civil es: {estado}")
    print(f"La edad es: {cifra_edad}")
    print(f"El genero es: {genero}")
else: print("No se pudo continuar por problemas en los datos ingresados")