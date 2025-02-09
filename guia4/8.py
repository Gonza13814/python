"""8) esPrimo, que devuelva si un número entero dado como parámetro es o no primo. """

def esPrimo(numero):
    return not (numero % 2 == 0 and numero % numero == 0) or (numero % 3 == 0 and numero % numero == 0) or (numero % 5 == 0 and numero % numero == 0) or (numero % 7 == 0 and numero % numero == 0)

 

print(esPrimo(6))

print("soy gay")

print("ES GAY")