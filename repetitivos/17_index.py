import os, math
os.system("cls")

print(f"   omar  ".index("o"))

def busca(texto, letra):
    i=0
    while texto[i]!=letra:
        i += 1
    return i
        
print(f"{busca('  omar','o')}")