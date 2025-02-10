"""8) Realizá un programa que permita al usuario ingresar dos números enteros, que representan las
medidas en grados de dos ángulos interiores de cierto triángulo. La computadora debe mostrar el
valor en grados del ángulo restante"""

medida1 = int(input("Ingrese la medida del primer angulo interior (grados) de un triangulo "))
medida2 = int(input("Ingrese la medida del segundo angulo interior (grados) de un triangulo "))

SUMA_DE_ANGULOS_TRIANGULO = 180

anguloRest = SUMA_DE_ANGULOS_TRIANGULO - medida1 - medida2

print(f"El valor del angulo restante es de {anguloRest}° ")

