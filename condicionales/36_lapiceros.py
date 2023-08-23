import os, math
os.system("cls")

cuadernos = int(input("Numero de cuadernos: "))

lucas = 0
faber = 0
pilot = 0
lapiceros = True

if cuadernos < 12:
    lapiceros = False
elif cuadernos in range(12, 24):
    lucas = (cuadernos//4)
elif cuadernos in range(24, 36):
    faber = 2 * (cuadernos//4)
elif cuadernos >= 36:
    pilot = 2 * (cuadernos//4)
    faber = cuadernos//6
    lucas = cuadernos//12

print(f"Los lapiceros Lucas obsequiados son: {lucas}")
print(f"Los lapiceros Faber obsequiados son: {faber}")
print(f"Los lapiceros Pilot obsequiados son: {pilot}")