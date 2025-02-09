"""13) Realizá un programa que permita al usuario ingresar números hasta que se introduzca un 0. La
computadora debe mostrar el número máximo y el número mínimo"""

num = int(input("Ingrese un número: "))
max = num
min = num

while not num == 0:
    num = int(input("Ingrese un número nuevamente: "))

    if (num < min and num != 0):
        min = num

    if (num > max):
        max = num
    

print(f"El numero máximo fue {max} y el minimo fue {min}")


