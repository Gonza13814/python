"""9) Realizá un programa que permita al usuario ingresar un número natural n. La computadora debe
mostrar los primeros n múltiplos de 3 excepto aquellos que sean a la vez múltiplos de 5"""

i = 0
numero = 10

while i < numero:
    if not i % 5 == 0:
        print(i * 3)
    else:
        numero += 1
    
    i += 1


