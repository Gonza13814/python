"""15) Realizá un programa que permita al usuario ingresar números mientras el promedio entre todos
los ingresados sea menor a 20. La computadora debe indicar la cantidad de valores leídos. """

promedio = 0
cantidad = 0
valorAcumulado = 0

while promedio < 20:
    num = int(input("Ingrese el numero: "))
    
    valorAcumulado += num
    cantidad += 1
    promedio = valorAcumulado / cantidad

print(f"La cantidad de valores leídos es {cantidad}")

