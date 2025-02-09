"""4) Realizá un programa que permita al usuario ingresar 5 edades. La computadora debe indicar
cuántas edades fueron valores impares mayores que 18."""

cantidadDeEdadesImpares = 0

for i in range (0 , 5):
    edad = int(input(f"Ingrese la edad {i + 1}: "))
    
    if edad > 18 and edad % 2 == 1:
        cantidadDeEdadesImpares += 1
    
    
print(f"La cantidad de edades impares es {cantidadDeEdadesImpares}")
