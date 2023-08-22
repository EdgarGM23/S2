import os
os.system("cls")

monto = float(input("Monto de la compra: "))

if monto > 5000: prestamo = 0.3
else: prestamo = 0.2

pago_propio = monto * (1 - prestamo)
pago_banco = (monto * prestamo) * 1.1

print(f"La empresa tendra que pagar de su propio dinero: S/{pago_propio:.2f}")
print(f"La empresa tendra que pagar el prestamo del banco: S/{pago_banco:.2f}")