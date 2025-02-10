"""
2) Realizá un programa que permita al usuario ingresar dos números enteros num1 y num2, donde el
primero siempre deberá ser menor o igual al segundo. La computadora debe mostrar la secuencia
de números existentes entre ambos:
A) Incluyendolos
B) Excluyendolos

"""

numA = int(input("Ingrese el primer numero: "))
numB = int(input("Ingrese el segundo numero: "))

#Incluyendolos
for i in range(numA , numB + 1):
    print(i)

#Excluyendolos
for i in range(numA + 1 , numB):
    print(i)

