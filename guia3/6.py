"""6) Realizá un programa que permita al usuario ingresar un número entero cant. Acto seguido, que
permita ingresar cant números reales, correspondientes a las estaturas de un equipo de jugadores
de baloncesto (en metros). La computadora debe mostrar la estatura promedio."""

sumaDeAlturas = 0
cant = int(input("Ingrese la cantidad de jugadores: "))

for i in range(0, cant):
    altura = float(input(f"Ingrese la altura (en metros) del jugador {i + 1}: "))
    sumaDeAlturas += altura

print(f"La altura promedio del equipo es de {sumaDeAlturas / cant}") 


