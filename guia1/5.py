"""5) Realizá un programa que permita al usuario ingresar el valor unitario de cierto artículo y la
cantidad de artículos vendidos por un vendedor, del cual se sabe que gana un sueldo fijo de $14000
más el 16% del monto total vendido. Con tales datos, la computadora debe calcular el sueldo
mensual del vendedor y mostrarlo. """

PrecioArt = float(input("Ingrese el precio del articulo: "))
CantidadArt = int(input("Ingrese la cantidad de articulos vendidos: "))

Salario = 14000 + (PrecioArt * CantidadArt) * 0.16

print("El salario mensual del vendedor es de " + str(Salario))

