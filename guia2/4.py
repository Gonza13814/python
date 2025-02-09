"""4) Realizá un programa que permita al usuario ingresar tres números enteros. La computadora debe
indicar cuál de ellos es el mayor."""

numA = int(input("Ingrese el primer número entero: "))
numB = int(input("Ingrese el segundo número entero: "))
numC = int(input("Ingrese el tercer número entero: "))

if numA >= numB and numA >= numC:
    print(f"{numA} es el mayor de los 3 numeros ingresados")
elif numB >= numA and numB >= numC:
    print(f"{numB} es el mayor de los 3 numeros ingresados")
elif numC >= numA and numC >= numB:
    print(f"{numC} es el mayor de los 3 numeros ingresados")


   


