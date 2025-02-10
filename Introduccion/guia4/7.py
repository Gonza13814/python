"""7) cantDivisores, que devuelva la cantidad de divisores que posea un número entero dado como parámetro."""


def cantDivisores(numero):
    cantidad = 0
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            cantidad += 1
    return cantidad

print(cantDivisores(5))

#Me ayudo el CHAT-GTP

