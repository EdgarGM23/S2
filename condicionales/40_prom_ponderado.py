import os, math
os.system("cls")

mat_PC1 = float(input("Matematica practica 1: "))
mat_PC2 = float(input("Matematica practica 2: "))
mat_PC3 = float(input("Matematica practica 3: "))
mat_EP = float(input("Matematica parcial: "))
mat_EF = float(input("Matematica final: "))

fis_PC1 = float(input("Fisica practica 1: "))
fis_PC2 = float(input("Fisica practica 2: "))
fis_PC3 = float(input("Fisica practica 3: "))
fis_EP = float(input("Fisica parcial: "))
fis_EF = float(input("Fisica final: "))

qui_PC1 = float(input("Quimica practica 1: "))
qui_PC2 = float(input("Quimica practica 2: "))
qui_PC3 = float(input("Quimica practica 3: "))
qui_EP = float(input("Quimica parcial: "))
qui_EF = float(input("Quimica final: "))

mat_promedio = (mat_PC1*0.1)+(mat_PC2*0.2)+(mat_PC3*0.1)+(mat_EP*0.3)+(mat_EF*0.3)
fis_promedio = (fis_PC1*0.2)+(fis_PC2*0.2)+(fis_PC3*0.2)+(fis_EP*0.2)+(fis_EF*0.2)
qui_promedio = (qui_PC1*0.1)+(qui_PC2*0.3)+(qui_PC3*0.1)+(qui_EP*0.25)+(qui_EF*0.25)

if mat_promedio >= 13: print(f"Aprobó con {mat_promedio:.2f} de nota")
else: print(f"Desaprobó con {mat_promedio:.2f} de nota")
if fis_promedio >= 13: print(f"Aprobó con {fis_promedio:.2f} de nota")
else: print(f"Desaprobó con {fis_promedio:.2f} de nota")
if qui_promedio >= 13: print(f"Aprobó con {qui_promedio:.2f} de nota")
else: print(f"Desaprobó con {qui_promedio:.2f} de nota")