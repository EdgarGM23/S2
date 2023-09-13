import os, operator
os.system("cls")

Pamela = int(input("Pamela: "))
Karol = int(input("Karol: "))
Fany = int(input("Fany: "))

mitad = (Pamela + Karol + Fany) // 2

mensaje = ""

if Pamela > mitad + 1 : mensaje = "Ganó Pamela"
elif Karol > mitad + 1 : mensaje = "Ganó karol"
elif Fany > mitad + 1: mensaje = "Ganó Fany"

elif Pamela < Karol and Pamela < Fany: mensaje = "Pasan a la segunda vuelta: Karol y Fany"
elif Karol < Pamela and Karol < Fany: mensaje = "Pasan a la segunda vuelta: Pamela y Fany"
elif Fany < Karol and Fany < Pamela: mensaje = "Pasan a la segunda vuelta: Karol y Pamela"

elif Pamela == Karol and Pamela == Fany and Karol == Fany: mensaje = "Elecciones anuladas"
elif Pamela > Karol and Pamela > Fany and Karol == Fany: mensaje = "Elecciones anuladas"
elif Karol > Pamela and Karol > Fany and Pamela == Fany: mensaje = "Elecciones anuladas"
elif Fany > Pamela and Fany > Karol and Pamela == Karol: mensaje = "Elecciones anuladas"

lista = {"Pamela: ": Pamela, "Karol: ": Karol, "Fany: ": Fany}
orden = sorted(lista.items(), key=operator.itemgetter(1), reverse=True)

print(mensaje)
print(f"1er Lugar: {orden[0]}")
print(f"2do Lugar: {orden[1]}")
print(f"3er Lugar: {orden[2]}")