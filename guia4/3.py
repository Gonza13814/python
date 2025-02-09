"""3) imprimirSimbolo, que imprima por consola n veces un caracter en la misma línea. Tanto n como el caracter se reciben como parámetro."""

def ImprimirSimbolo(texto, cantidad):
    for _ in range(0, cantidad):
        print(texto)

ImprimirSimbolo("hola", 5)

