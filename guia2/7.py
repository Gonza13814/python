"""7) Realizá un programa que permita al usuario ingresar tres números. La computadora debe
mostrarlos ordenados de menor a mayor."""


numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número: "))
numC = int(input("Ingrese el tercer número: "))

if numA <= numB and numA <= numC:
    if numB <= numC:
        print(f"El orden de menor a mayor queda así: {numA} {numB} {numC}.")
    else:
        print(f"El orden de menor a mayor queda así: {numA} {numC} {numB}.")
elif numB <= numA and numB <= numC:
    if numA <= numC:
        print(f"El orden de menor a mayor queda así: {numB} {numA} {numC}.")
    else:
        print(f"El orden de menor a mayor queda así: {numB} {numC} {numA}.")
elif numC <= numA and numC <= numB:
    if numA <= numB:
        print(f"El orden de menor a mayor queda así: {numC} {numA} {numB}.")
    else:
        print(f"El orden de menor a mayor queda así: {numC} {numB} {numA}.")






