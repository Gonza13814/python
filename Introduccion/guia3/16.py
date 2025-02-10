"""16) Realizá un programa que permita al usuario ingresar números enteros. Por cada carga debe
preguntar si se desea seguir ingresando, de la forma "¿Deseás ingresar otro número? [S/N]".
La carga de datos finaliza cuando se detecta una 'n' o 'N'. Reutilizá el algoritmo realizado en el
ejercicio 12) para validar la opción ingresada. La computadora debe mostrar el porcentaje de
números pares ingresados."""

pregunta = "s"
porcentajePares = 0
pares = 0
numerosTotales = 0

while not (pregunta == "N" or pregunta == "n"):
    num = int(input("Ingrese un número entero: "))

    numerosTotales += 1
   
    if num % 2 == 0:
        pares += 1

    pregunta = str(input("¿Deseas ingresar otro número? Indique si SI (S) o si NO (N). "))


porcentajePares = pares / numerosTotales

print(f"El porcentaje de numeros pares es de {porcentajePares}")


