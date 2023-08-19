import os
os.system("cls")

numero4cifras = int(input("Numero: "))

mayor=0
menor=0

cifra1 = numero4cifras//1000
cifra2 = (numero4cifras%1000)//100
cifra3 = ((numero4cifras%1000)%100)//10
cifra4 = ((numero4cifras%1000)%100)%10

if cifra1 > cifra2 and cifra1 > cifra3 and cifra1 > cifra4: mayor = cifra1
elif cifra2 > cifra1 and cifra2 > cifra3 and cifra2 > cifra4: mayor = cifra2
elif cifra3 > cifra2 and cifra3 > cifra4 and cifra3 > cifra4: mayor = cifra3
elif cifra4 > cifra1 and cifra4 > cifra2 and cifra4 > cifra3: mayor = cifra4

if cifra1 < cifra2 and cifra1 < cifra3 and cifra1 < cifra4: menor = cifra1
elif cifra2 < cifra1 and cifra2 < cifra3 and cifra2 < cifra4: menor = cifra2
elif cifra3 < cifra2 and cifra3 < cifra4 and cifra3 < cifra4: menor = cifra3
elif cifra4 < cifra1 and cifra4 < cifra2 and cifra4 < cifra3: menor = cifra4

print(mayor,menor)