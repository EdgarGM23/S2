import os
os.system("cls")

codigo = int(input("Codigo: "))

bDiv2 = codigo%2 == 0
bDiv3 = codigo%3 == 0
bDiv5 = codigo%5 == 0

if bDiv2 and bDiv3 and bDiv5:
    print("El empleado es Administrativo")
elif not bDiv2 and bDiv3 and bDiv5:
    print("El empleado es Diretivo")
elif bDiv2 and not bDiv3 and not bDiv5:
    print("El empleado es Vendedor")
elif not bDiv2 and not bDiv3 and not bDiv5:
    print("El empleado es Seguridad")
else: print("No hay tipo")