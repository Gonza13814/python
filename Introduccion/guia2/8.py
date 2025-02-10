"""8) Realizá un programa que permita al usuario ingresar dos números enteros. La computadora debe
indicar si el mayor es divisible por el menor."""

numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número: "))

mayor = 0
menor = 0

if not numA == numB:
    if numA > numB:
        mayor = numA
        menor = numB
    else:
        mayor = numB
        menor = numA
    
    if not menor == 0: 
        if mayor % menor == 0:
            print(f"{mayor} es divisible por {menor}")
        else:
            print(f"{mayor} no es divisible por {menor}")
    else:
        print("No es posible dividir por 0")
else:
    print("Los numero son iguales")






"""
if numA >= numB and numA % numB == 0:
    print(f"{numA} es divisible por {numB}")
elif numB >= numA and numB % numA == 0:
    print(f"{numB} es divisible por {numA}")
else:
    print("Ninguno de los números son divisibles entre sí.")
"""





