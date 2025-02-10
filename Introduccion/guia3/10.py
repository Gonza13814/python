"""10) Realizá un programa que permita validar una nota de examen. Se espera que la nota que el
usuario ingrese sea un número comprendido entre 0 y 10. La misma debe ser tantas veces ingresada
como sean necesarias hasta que quede comprendida dentro del rango descripto."""

nota = int(input("Ingrese la nota del exámen (entre 0 y 10): "))

while not (nota >= 0 and nota <= 10):
    nota = int(input("Nota inválida. Ingrese la nota del exámen nuevamente (entre 0 y 10): "))

    
