
# Mensaje al usuario
print("Señor(a) usuarios ingrese la cantidad de gaones que desear tener de leche: ")

try:
    # Pedir la cantidad en litros que desea producir
    cantidad = int(input("Ingrese la cantidad de litros que vas a producir: "))

    # Pedir el precio que tendra cada galon
    precio = int(input("Ingrese el precio que tendra cada galon: "))
except ValueError:
    print("Por favor ingrese valores numericos validos.")
    exit()

# 1 galon es igual a 7.785
galon = 3.785

# Operacion de conversion para la cantidad de litros ingresada se convierta por la cantidad de galones
totalGalones = cantidad / galon

# Mensaje del total de galones
print(f"Galones =  {totalGalones:.2f}")

# Operacion para calcular el total de galones por el precio
totalPrecio = totalGalones * precio

# Salida de los datos
print(f"Cantidad de litros ingresado: {cantidad:.2f}")
print(f"Convertido a galones: {totalGalones:.2f}")
print(f"El precio total es: {totalPrecio:.2f}")


