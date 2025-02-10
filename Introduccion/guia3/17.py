"""17) Realizá un programa que permita al usuario ingresar la cantidad de cierto artículo y el precio
unitario de dicho artículo. Por cada carga debe preguntar si se desea seguir ingresando de la forma
"¿Deseás ingresar otro artículo? [S/N]". La carga de datos finaliza cuando se detecta una
'n' o 'N'. Reutilizá el algoritmo realizado en el ejercicio 12) para validar la opción ingresada. La
computadora debe mostrar el monto total del ticket"""


pregunta = "s"
total = 0

while not (pregunta == "N" or pregunta == "n"):
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    parcial = cantidad * precio

    total += parcial

    pregunta = str(input("¿Deseas ingresar otro número? Indique si SI (S) o si NO (N). "))


print(f"El monto total del ticket es {total}.")
