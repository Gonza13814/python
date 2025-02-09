"""12) Realizá un programa que permita al usuario ingresar su edad (entre 1 y 120 años) y su género
('F' o 'M'). La computadora debe indicar si la persona está o no en edad de jubilarse"""

def edadJubilatoria(edad, genero):
    if (edad >= 60 and genero == "F") or (edad >= 65 and genero == "M"):
        print("Está en edad de jubilarse.")
    else:
        print("No está en edad de jubilarse.")

edadJubilatoria(65, 'M')


