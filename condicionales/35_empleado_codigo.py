import os
os.system("cls")

codigo = int(input("Codigo: "))

if codigo%2 == 0 and codigo%3 == 0 and codigo%5 == 0:
    print("El empleado es Administrativo")
elif codigo%2 != 0 and codigo%3 == 0 and codigo%5 == 0:
    print("El empleado es Diretivo")
elif codigo%2 == 0 and codigo%3 != 0 and codigo%5 != 0:
    print("El empleado es Vendedor")
else:
    print("El empleado es Seguridad")