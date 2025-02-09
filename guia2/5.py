"""5) Realizá un programa que permita al usuario ingresar su edad (entre 1 y 120 años) y su género
('F' para mujeres, 'M' para hombres). La computadora debe indicar si la persona está en edad de
jubilarse. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido),
informar tal situación"""

edad = int(input("Ingrese su edad (entre 0 y 120): "))
genero = str(input("Ingrese su genero (M para hombres, F para mujeres): "))

edad_de_jubilación_masculina = 65
edad_de_jubilación_femenina = 60

if not(edad >= 120 or edad <= 0):
    if (genero == "F" or genero == "M"):
        if (edad >= 65) or (genero == "F" and edad >= 60):
            print("se jubila")
        else:
            print("No se jubila")
    else:
        print("Genero invalido")
else: 
    print("Edad invalida")


"""
if 0 >= edad or edad >= 120:
    print("Edad inválida. Debe ingresar una edad entre 0 y 120 años.")
elif genero == "M" and edad >= edad_de_jubilación_masculina or genero == "F" and edad >= edad_de_jubilación_femenina:
    print("Usted esta en edad de jubilarse.")
elif genero == "M" and edad < edad_de_jubilación_masculina or genero == "F" and edad < edad_de_jubilación_femenina:
    print("Usted no esta en edad de jubilarse")
elif genero != "M" or genero != "F":
    print("Genero inválido. Debe ingresar una (M) si es hombre, o una (F) si es mujer.")

"""





