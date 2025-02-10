"""9) Realizá un programa que permita al usuario ingresar los lados a, b y c de un triángulo. La
computadora informa si el triángulo es o no válido. En caso afirmativo, además informa si es
equilátero, isósceles o escaleno."""

ladoA = int(input("Ingrese la longitud del primer lado: "))
ladoB = int(input("Ingrese la longitud del segundo lado: "))
ladoC = int(input("Ingrese la longitud del tercer lado: "))

if not (ladoA > ladoB + ladoC or ladoB > ladoA + ladoC or ladoC > ladoA + ladoB):
    if ladoA == ladoB == ladoC:
        print("Su triángulo es Equilátero.")
    elif (ladoA == ladoB and ladoC != ladoA) or (ladoB == ladoC and ladoA != ladoB) or (ladoA == ladoC and ladoB != ladoA):
        print("Su triángulo es Isósceles.")
    elif ladoA != ladoB != ladoC:
        print("Su triángulo es Escaleno.")
else:
    print("Su triángulo no es válido.")



#Me falto la parte de: ¿Qué pasa si pongo un n° de lado negativo? Hecho por el petero ↓↓↓


"""if not((ladoA <= 0 or ladoB <= 0 or ladoC <= 0) or (ladoA > (ladoB + ladoC) or ladoB > (ladoA + ladoC) or ladoC > (ladoB + ladoA))):
    if ladoA == ladoB and ladoB == ladoC:
        print("El triangulo es equilatero")
    elif ladoA == ladoB and ladoB != ladoC:
        print("El triangulo es isosceles")
    elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
        print("El triangulo es escaleno")
else: 
    print("El triangulo es invalido")"""


