import os
os.system("cls")

def mayus(texto):
    if texto=="": return ""
    rpta = ""
    for i in texto:
        rpta += chr(ord(i) - 32) if i >= "a" and i <= "z" else i
    return rpta

print(mayus("omar"))