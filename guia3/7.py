"""7) Realizá un programa que permita al usuario ingresar un número entero cant. Acto seguido, que
permita ingresar cant números enteros. La computadora debe mostrar cuál fue el mayor número y
en qué posición apareció."""

mayor = 0
posición = 0
cant = int(input("Ingrese la cantidad de números: "))

for i in range(0, cant):
    numero = int(input(f"Ingrese el valor del número {i + 1}: "))
    
    if numero >= mayor:
        mayor = numero
        posición = i + 1


print(f"El mayor número fue {mayor} en la posición {posición}")
