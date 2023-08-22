import os, random
os.system("cls")

linea = ""

for i in range(1,11):
    numero = random.randrange(1,100)
    linea += str(numero) + (", " if i<10 else "")
print(linea)