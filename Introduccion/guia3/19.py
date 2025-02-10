"""19) Realizá un programa que permita al usuario ingresar dos números enteros que representen el
ancho y el alto de una matriz de cruces. La computadora debe mostrar dicha matriz."""

ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))

for _ in range (0, alto):
    for _ in range(0, ancho):
        print("X", end=" ")
    print("")
