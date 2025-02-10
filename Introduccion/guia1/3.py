"""
3) Realizá un programa que permita al usuario ingresar el valor salarial de una hora de trabajo y la
cantidad de horas trabajadas por día. La computadora debe mostrar el valor del salario semanal,
asumiendo que trabaja todos los días hábiles y media jornada los sábados

"""
salario = float(input("Ingrese su salario (por hora): "))
horas = int(input("Ingrese las horas a trabajar (por día): "))

salarioSemanal = (salario * horas) * 5.5

print("Su salario semanal es: " + str(salarioSemanal))



