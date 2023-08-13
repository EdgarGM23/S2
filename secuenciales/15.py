import os
os.system("cls")

juan = int(input("Ingrese el dinero de Juan: "))
rosa = int(input("Ingrese el dinero de Rosa: "))
daniel = int(input("Ingrese el dinero de Daniel: "))

danielDolar = daniel / 3

total = juan + rosa + danielDolar

Pjuan = juan*100/total
Prosa = rosa*100/total
Pdaniel = danielDolar*100/total

print("El total es: ", total,"\n", "EL porcetaje de cada uno es: ")
print("Juan: ", round(Pjuan,2),"%")
print("Rosa: ", round(Prosa,2),"%")
print("Daniel: ", round(Pdaniel,2),"%")