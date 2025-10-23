from datetime import datetime 

# Validar al momento de pedir datos
try:
    anfitrion = input("Ingrese el nombre de la persona responsable: ")
    cantidadPersonas = int(input("¿Cuantas personas asistiran al evento?: "))
except ValueError:
    print("Por favor ingrese un numero valido para la cantidad de personas.")
    exit()

fecha = datetime.now()

# Valor del plato por persona original 
ValorPlatoGeneral = 95

# Se verifica si la cantidad de personas entre mayor a 200 y menor que 300 es valido y cambia su valor del plato.
# Pero si la cantidad de personas es mayor que 300 se cambia el valor del plato.

if cantidadPersonas > 200 and cantidadPersonas <= 300:
    plato = 85

    # Operacion del valor del valor por la cantidad de personas
    operacion = plato * cantidadPersonas

    # Mostrar datos en la salida 
    print(f"Fecha: {fecha}")
    print(f"Nombre de la persona responsable: {anfitrion}")
    print(f"Cantidad de personas: {cantidadPersonas}")
    print(f"Valor del plato: ${plato}")
    print(f"Total a pagar: {operacion}")
elif cantidadPersonas > 300: 
    plato = 75

    # Operacion del valor del valor por la cantidad de personas
    operacion = plato * cantidadPersonas

    # Mostrar datos en la salida 
    print(f"Fecha: {fecha}")
    print(f"Nombre del anfitrion: {anfitrion}")
    print(f"Cantidad de personas: {cantidadPersonas}")
    print(f"Valor del plato: ${plato}")
    print(f"Total a pagar: {operacion}")
else: 

    # Operacion del valor del valor por la cantidad de personas
    operacion = ValorPlatoGeneral * cantidadPersonas

    # Mostrar datos en la salida 
    print(f"Fecha: {fecha}")
    print(f"Nombre de la persona responsable: {anfitrion}")
    print(f"Cantidad de personas: {cantidadPersonas}")
    print(f"Valor del plato: ${ValorPlatoGeneral}")
    print(f"Total a pagar: {operacion}")