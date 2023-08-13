import os
os.system("cls")

monto = int(input("Ingrese el monto: "))
docientos = 0
cien = 0
cincuenta = 0
veinte = 0
dies = 0
cinco = 0
dos = 0
uno = 0

while monto >= 200:
    docientos += 1
    monto -= 200
while monto >= 100:
    cien +=1
    monto -= 100
while monto >= 50:
    cincuenta += 1
    monto -= 50
while monto >= 20:
    veinte += 1
    monto -= 20
while monto >=10:
    dies += 1
    monto -= 10
while monto >=5:
    cinco += 1
    monto -= 5
while monto >=2:
    dos += 1
    monto -= 2
while monto >=1:
    uno += 1
    monto -= 1

print("---------------------------------------------")

print("Billetes: ")
print("\n",docientos,"billetes de 200","\n", cien,"billete de 100","\n", cincuenta,"billete de 50","\n", veinte,"billetes de 20","\n", dies,"billete de 10","\n")
print("Monedas: ")
print("\n",cinco,"moneda de 5","\n", dos,"monedas de 2","\n", uno,"moneda de 1","\n")