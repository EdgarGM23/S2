import os
os.system("cls")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

Primeracifra1 = numero1 % 10
Primeracifra2 = (numero1 // 10)%10
Primeracifra3 = (numero1 // 100)%10

Segundacifra1 = numero2 % 10
Segundacifra2 = (numero2 // 10)%10
Segundacifra3 = (numero2 // 100)%10

print(Segundacifra1, Primeracifra2, Segundacifra3," y ", Primeracifra1, Segundacifra2, Primeracifra3)