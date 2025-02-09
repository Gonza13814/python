"""8 esPrimo, que devuelva si un número entero dado como parámetro es o no primo. """

def esPrimo(numero):
    divisoresDelNumero = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisoresDelNumero += 1
    
    return divisoresDelNumero == 2

print(esPrimo(13))

