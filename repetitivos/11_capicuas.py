import os
os.system("cls")

contador = 0

for i in range(100,1000):
    
    cifra1 = i // 100
    cifra2 = (i // 10) % 10
    cifra3 = i % 10
    
    patron1=cifra1,cifra3
    patron2=cifra3,cifra1
    
    if patron1==patron2: 
        print(i)
        contador += 1
print(f"Hay {contador} numeros capicuas")
