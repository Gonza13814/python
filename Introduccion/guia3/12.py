"""12) Realizá un programa que permita validar una opción ingresada. La computadora preguntará al
usuario si desea continuar una operación de la forma "¿Deseás continuar? [S/N]". Se espera
que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser tantas veces
ingresada como sean necesarias hasta que quede comprendida dentro de las posibilidades
esperadas."""

opcion = str(input("¿Deseas continuar con la operación? Indique si SI (S) o si NO (N)."))

while not (opcion == "S" or opcion == "N" or opcion == "s" or opcion == "n"):
    opcion = str(input("Opción Incorrecta. ¿Deseas continuar con la operación? Indique si SI (S) o si NO (N)."))

    


