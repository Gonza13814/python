"""8) Realizá un programa que permita al usuario ingresar un número natural. La computadora debe
mostrar el factorial del número. """

numero = 4
resultado = 1

for i in range (1, numero + 1):
    resultado *= i

print(f"El factorial de {numero} es {resultado}")

