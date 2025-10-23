from datetime import datetime 

# Pedir datos

try:
    # El usuario debe ingresar el valor de su traje
    valor_compra = float(input("Ingrese el valor de su compra: ")) 

    # El usuario debe ingresar su nombre
    nombre = input("Ingrese su nombre por favor: ")

    # El usuario debe ingresar su numero de documento
    documento = int(input("Nombre su n° de documento: "))

except ValueError:
    print("Por favor ingrese valores numericos validos.")
    exit()

fecha = datetime.now()

# El sistema verificara si el valor del traje o de su compra es mayor o menor que 2500
if valor_compra > 2500:

    # Si es mayor se le aplica un descuento del 15%

    # Operacion de resta para sacar el descuento dependiendo del valor de la compra
    descuento = valor_compra * 0.15

    # Operacion de resta para sacar el total
    total = valor_compra - descuento
    print("Se le aplica el descuento de 15%")

    # Salida de los datos
    print(f"El cliente: {nombre}")
    print(f"N° de documento: {documento}")
    print(f"Fecha: {fecha}")
    print(f"Valor del descuento: {descuento}")
    print(f"Pago total: {total}")
else: 

    # Si es menor se le aplica un descuento del 8%

    # Operacion de resta para sacar el descuento dependiendo del valor de la compra
    descuento = valor_compra * 0.08

    # Operacion de resta para sacar el total
    total = valor_compra - descuento
    print("Se le aplica el descuento de 8%")

    # Salida de los datos
    print(f"El cliente: {nombre}")
    print(f"N° de documento: {documento}")
    print(f"Fecha: {fecha}")
    print(f"Valor del descuento: {descuento}")
    print(f"Pago total: {total}")