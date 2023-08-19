import os
os.system("cls")

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
nota4 = int(input("Nota 4: "))
nota5 = int(input("Nota 5: "))

notas = [nota1, nota2, nota3, nota4, nota5]

notas.sort()

promedio = (notas[1] + notas[2] + notas[3]) /3

print(f"La notas eliminadas son: {notas[0]} y {notas[4]}")
print(f"El promedio aprobatorio es: {promedio:.2f}")