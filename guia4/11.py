"""11) Realizá un programa que permita al usuario ingresar el valor unitario de cierto artículo y la
cantidad de artículos vendidos por un vendedor, del cual se sabe que gana un sueldo fijo de $14000
más el 16% del monto total vendido. Con tales datos, la computadora debe calcular el monto a
cobrar por el vendedor y mostrarlo."""

porcentajeVentas = 0.16
sueldoFijo = 14000

def calcularSueldo(precio, cantidad):
    return (precio * cantidad) * porcentajeVentas + sueldoFijo

print(f"El sueldo total es {calcularSueldo(100, 10)}.")

