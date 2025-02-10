"""
2) Realizá un programa que permita al usuario ingresar 3 notas pertenecientes a tres trimestres
distintos para cierto alumno. La computadora debe mostrar la nota promedio. 

"""
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("La nota promedio del alumno es: "+ str(int(promedio)))