"""5) Realizá un programa que permita al usuario ingresar un número entero cant. Acto seguido, que
permita ingresar cant números reales, correspondientes a las ventas realizadas por cierto
vendedor. La computadora debe mostrar el total de las ventas"""

total = 0
cant = int(input("Ingrese la cantidad de ventas: "))

for i in range(0, cant):
    valor = int(input(f"Ingrese el valor de la venta {i + 1}: "))
    total += valor

print(f"El total de ventas es de {total}")

