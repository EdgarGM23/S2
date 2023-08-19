import os
os.system("cls")

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

if nota3 >= 10: nota3 += 2

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio de notas es: {promedio:.2f}")