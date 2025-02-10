"""7) Realizá un programa que permita al usuario ingresar dos números enteros. La computadora debe
mostrar los resultados de las 4 operaciones matemáticas básicas con tales números. """

num1 = int(input("Ingrese un numero entero "))
num2 = int(input("Ingrese un numero entero nuevamente "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
división = num1 / num2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {división}")

