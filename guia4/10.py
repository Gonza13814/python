"""10) esNumeroPerfecto, que devuelva si un número entero dado como parámetro es o no perfecto."""

# Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos. 
# Dicho de otra forma, un número perfecto es aquel que es amigo de sí mismo. 
# Así, 6 es un número perfecto porque sus divisores propios positivos son 1, 2 y 3; y 6 = 1 + 2 + 3.

numero = 4
cantidad = 0

for i in range(1, numero + 1):
    cantidad += i
    if numero % cantidad == 0:
        print("Es PERFECTO")

"""numero = 3
cantidad = 0

def esNumeroPerfecto(numero):
    for i in range(1, numero + 1):
        cantidad += i
    return numero == cantidad


print(f"El numero es {cantidad}")   #¿Por qué si pongo la frase me lo suma, pero sino no?"""