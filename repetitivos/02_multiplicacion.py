import os
os.system("cls")

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

def multi(num1, num2):
    resultado = 0
    while num2 >= 1:
        resultado += num1
        num2 -= 1
    return resultado

print(f"El resultado es: {multi(numero1, numero2)}")