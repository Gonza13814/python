"""13) Realizá un programa que permita al usuario ingresar la cantidad de cierto producto y el precio
unitario de dicho producto. Por cada carga debe preguntar si se desea seguir ingresando de la forma
"¿Deseás ingresar otro artículo? [S/N]". La carga de datos finaliza cuando el usuario lo
determine. La computadora debe mostrar el monto total del ticket."""

"""def montoTotal(precio, cantidad):
    print(f"Su monto parcial es {precio * cantidad}")

    pregunta = print(str(input("¿Deseás ingresar otro artículo? [S/N]: ")))
    total = precio * cantidad

    while not (pregunta == "n" or  pregunta == "N"):
        precio = int(input("Ingrese otro precio: "))
        cantidad = int(input("Ingrese otra cantidad: "))

        montoParcial = precio * cantidad

        total += montoParcial
        pregunta = print(str(input("¿Deseás ingresar otro artículo? [S/N]: ")))

        print(f"Su monto total es {total}.")


montoTotal(100, 200)"""

def main():
    confirmar = ''
    montoTotal = 0
    while not (confirmar == 'N' or confirmar == 'n'):
        cantidad = int(input("ingrese la cantidad: "))
        precio = int(input("ingrese el precio: "))

        montoTotal += calcularMontoParcial(cantidad,precio)
        
        confirmar = str(input("Deseas continuar? si o no: "))

    print(f"El monto total es {montoTotal}")

def calcularMontoParcial(cantidad, precio):
    return cantidad * precio

main()

