import os
os.system("cls")

contador = 0

for i in range(1000,10000):
    pares = 0
    impares = 0
    
    cifra1 = i // 1000
    cifra2 = (i // 100) % 10
    cifra3 = (i // 10) % 10
    cifra4 = (i % 1000) % 10

    if cifra1%2==0: pares += cifra1
    if cifra2%2==0: pares += cifra2
    if cifra3%2==0: pares += cifra3
    if cifra4%2==0: pares += cifra4
    
    if cifra1%2!=0: impares += cifra1
    if cifra2%2!=0: impares += cifra2
    if cifra3%2!=0: impares += cifra3
    if cifra4%2!=0: impares += cifra4
    
    if pares == impares:
        print(f"{i}\n")
        contador += 1
    
print(f"La cantidad de numeros que cumplen la condicion son: {contador}")