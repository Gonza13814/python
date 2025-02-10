"""2) Realizá un programa que permita al usuario ingresar la cantidad de inscriptos a una conferencia
y la cantidad de asientos disponibles en el auditorio. La computadora debe indicar si alcanzan los
asientos, en caso contrario, indicar cuántos faltan para que todos los inscriptos puedan sentarse. """

inscriptos = int(input("Ingrese la cantidad de inscriptos: "))
asientos = int(input("Ingrese la cantidad de asientos disponibles: "))

if inscriptos <= asientos:
    print("Hay asientos disponibles para todos los inscriptos")
else:
    print(f"Asientos insuficientes. Serán necesarios {inscriptos - asientos} asientos más para que todos los inscriptos puedan sentarse.")


