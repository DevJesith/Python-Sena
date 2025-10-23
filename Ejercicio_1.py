import math

# Entrada de datos con validacion
try:
    H = float(input("Ingrese la longitud de la hipotenusa (H): "))
    R = float(input("Ingrese el valor del cateto R (también es el radio): "))

    # Verificamos que H sea mayor que R para que el calculo tenga sentido
    if H <= R:
        print("La hipotenusa debe ser mayor que el cateto R.")
        exit()

except ValueError:
    print("Por favor ingrese valores numericos validos.")
    exit()

# Calculo de la altura usando el teorema de Pitágoras
altura = math.sqrt(H**2 - R**2)
 
# Area del triangulo
area_triangulo = (R * altura) / 2

# Area de la semicircunferencia
area_semicirculo = (math.pi * R**2) / 2

# Area total
area_total = area_triangulo + area_semicirculo

# Mostrar resultados
print("\nResultados:")
print(f"Altura del triangulo: {altura:.2f}")
print(f"Area del triangulo: {area_triangulo:.2f}")
print(f"Area de la semicircunferencia: {area_semicirculo:.2f}")
print(f"Area total de la figura A: {area_total:.2f} unidades cuadradas")