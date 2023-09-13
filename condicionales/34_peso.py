import os, math
os.system("cls")

peso = float(input("Peso: "))
estatura = float(input("Estatura: "))

imc = peso / (math.pow(estatura,2))

if imc < 20: grado_obesidad = "Delgado"
elif imc >= 20 and imc <25: grado_obesidad = "Normal"
elif imc >= 25 and imc <=27: grado_obesidad = "Sobrepeso"
elif imc > 27: grado_obesidad = "Obesidad"

print(f"{imc:.2f}")
print(f"El grado de obesidad es:    {grado_obesidad}")