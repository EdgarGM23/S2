import os
os.system("cls")

#Entrada
varones=int(input("Varones: "))
mujeres=int(input("Mujeres: "))
total=varones+mujeres

Pvar=varones*100.0/total
Pmuj=mujeres*100.0/total

print("\n")

print("% de Varones: ","%.2f"%Pvar,"%")
print("% de Mujeres: ",round(Pmuj, 2),"%")

print("\n")

print(F"% de Varones: {format(Pvar,'.2f')}%")
print(F"% de Mujeres: {format(Pmuj,'.2f')}%")