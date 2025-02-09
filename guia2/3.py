"""3) Realizá un programa que permita al usuario ingresar dos números enteros. La computadora debe
indicar cuál de ellos es el mayor."""

numA = int(input("Ingrese el primer número entero: "))
numB = int(input("Ingrese el segundo número entero: "))

if numA > numB:
    print(f"{numA} es mayor que {numB}")
else:
    print(f"{numB} es mayor que {numA}")

    