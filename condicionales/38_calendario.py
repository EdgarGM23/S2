import os, math
os.system("cls")

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre","Octubre", "Noviembre", "Diciembre"]

if año%4==0 and año!=100 or año%400==0: bisiesto = True
else: bisiesto = False

enero = 31
if bisiesto: febrero = 29
else: febrero = 28
marzo = 31
abril = 30
mayo = 31
junio = 30
julio = 31
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

if mes == 1: days = enero
elif mes == 2: days = febrero
elif mes == 3: days = marzo
elif mes == 4: days = abril
elif mes == 5: days = mayo
elif mes == 6: days = junio
elif mes == 7: days = julio
elif mes == 8: days = agosto
elif mes == 9: days = septiembre
elif mes == 10: days = octubre
elif mes == 11: days = noviembre
elif mes == 12: days = diciembre

if mes == 1: contador = dia
elif mes == 2: contador = enero + dia 
elif mes == 3: contador = enero + febrero+ dia
elif mes == 4: contador = enero + febrero + marzo + dia
elif mes == 5: contador = enero + febrero + marzo + abril + dia
elif mes == 6: contador = enero + febrero + marzo + abril + mayo + dia
elif mes == 7: contador = enero + febrero + marzo + abril + mayo + junio + dia
elif mes == 8: contador = enero + febrero + marzo + abril + mayo + junio + julio + dia
elif mes == 9: contador = enero + febrero + marzo + abril + mayo + junio + julio + agosto + dia
elif mes == 10: contador = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + dia
elif mes == 11: contador = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + dia
elif mes == 12: contador = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + dia

print(f"Dias del mes:       {days}")
print(f"Mes:                {meses[mes-1]}")
print(f"Dias desde enero:   {contador}")