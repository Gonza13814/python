"""1) Realizá un programa que permita al usuario ingresar un número entero. La computadora debe
indicar si se trata de un número par o impar."""

num = int(input("Ingrese un numero entero: "))

if num % 2 == 0:
    print("Su número es par")
else: 
    print("Su número es impar")

