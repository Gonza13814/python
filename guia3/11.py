"""11) Realizá un programa que permita validar una nota de examen para cierta academia, de la misma
manera que el ejercicio anterior, pero con la siguientes nueva directiva:
Las notas válidas deberán ser el 2 y el rango comprendido entre el 4 y el 10."""

nota = int(input("Ingrese la nota del exámen (entre 0 y 10): "))

while not (nota == 2 or (nota >= 4 and nota <= 10)):
    nota = int(input("Nota inválida. Ingrese la nota del exámen nuevamente (entre 0 y 10): "))

