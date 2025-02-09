"""6) Realizá un programa que permita al usuario ingresar el ancho y el largo de un terreno en metros
y el valor del metro cuadrado de tierra. La computadora debe mostrar el valor total del terreno y la
cantidad de metros de alambre que serían necesarios para cercarlo completamente en tres pasadas."""


Ancho = int(input("Ingrese el ancho del terreno (metros) "))
Largo = int(input("Ingrese el largo del terreno (metros) "))
Valor = int(input("Ingrese el valor del metro cuadrado "))

ValorTerreno = Valor * Ancho * Largo
Alambre = 3 * Ancho * Largo

print("El valor del terreno es " + str(ValorTerreno))
print("La cantidad de metros de alambre para 3 vueltas es " +str(Alambre))

