"""6) esMultiplo, que devuelva si un número entero es múltiplo de otro. Ambos son dados como parámetros."""

def esMultiplo(numeroA, numeroB):
    return numeroA % numeroB == 0 or numeroB % numeroA == 0

print(esMultiplo(21, 7))

