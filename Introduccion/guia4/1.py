"""1) esPar, que devuelva si un número entero
dado como parámetro es par o no."""

def esPar(numero):
    return numero % 2 == 0

edad = 6
paridadDelNumero = esPar(edad)

print(paridadDelNumero)