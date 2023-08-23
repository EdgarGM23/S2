import os, math
os.system("cls")

def izstrip(texto):
    i = 0
    while texto[i] == " ": i += 1
    return texto[i:]

print(izstrip("    omar"))

def derstrip(texto):
    i = -1
    while texto[i] == " ": i -=1
    return texto[:i+1]

print(f'{derstrip("omar     ")}hola')

def todo_strip(texto):
    i = 0
    while texto[i] == " ": i += 1

    j = -1
    while texto[j] == " ": j -=1
    return texto[i:j+1]

print(f"{todo_strip('  omar  ')}hola")