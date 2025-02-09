"""6) Realizá un programa que permita al usuario ingresar la edad y el sueldo de cierto empleado. La
computadora muestra el monto del aporte al sindicato que se debe descontar del salario del
empleado, según el siguiente cuadro:
 
      Escala salarial            Porcentaje a descontar
     Menos de $20000                   0.7%
   Entre $20000 y $29999               1.4%
   Entre $30000 y $39999               2.1%
      $40000 o más                     2.8%

Además, si la persona tiene 30 años o menos, se cobra un 30% adicional del valor del aporte"""

edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su salario (en pesos argentinos): "))

COBRO_ADICIONAL = 1.3


if not edad <= 30:
    if sueldo < 20000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.007}.")
    elif sueldo >= 20000 and sueldo < 30000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.014}.")
    elif sueldo >= 30000 and sueldo < 40000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.021}.")
    elif sueldo >= 40000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.028}.")
else:
    if sueldo < 20000:

        print(f"El aporte destinado al sindicato es de {sueldo * 0.007 * COBRO_ADICIONAL}.")
    elif sueldo >= 20000 and sueldo < 30000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.014 * COBRO_ADICIONAL}.")
    elif sueldo >= 30000 and sueldo < 40000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.021 * COBRO_ADICIONAL}.")
    if sueldo >= 40000:
        print(f"El aporte destinado al sindicato es de {sueldo * 0.028 * COBRO_ADICIONAL}.")



    

       



