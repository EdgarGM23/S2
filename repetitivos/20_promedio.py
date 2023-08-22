import os
os.system("cls")

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))
numero4 = int(input("Numero 4: "))
numero5 = int(input("Numero 5: "))
numero6 = int(input("Numero 6: "))
numero7 = int(input("Numero 7: "))
numero8 = int(input("Numero 8: "))
numero9 = int(input("Numero 9: "))
numero10 = int(input("Numero 10: "))

lista = [numero1, numero2, numero3, numero4, numero5, numero6, numero7, numero8, numero9, numero10]

lista.sort()

promedio = (numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8 + numero9 + numero10) / 10

print(f"El numero mayor es: {lista[9]}")
print(f"El numero menor es: {lista[0]}")
print(f"El promedio es: {promedio:.2f}")
