"""14) Realizá un programa que permita al usuario ingresar los datos de cada uno de los 8 choferes de
una empresa de viajes en ómnibus:
▪ Edad [25 a 40] ▪ Antigüedad [5 a 30] ▪ Turno ('M'|'T'|'N')
Todos los choferes obtendrán un bono de 500 dólares. Los que tengan una antigüedad superior a la
mitad de su edad, cobrarán un 10% extra. Los del turno nocturno cobrarán otro 5% extra.
La computadora debe mostrar, de forma clara y ordenada:

A) El monto total que la empresa paga en concepto de bono para todos sus choferes.
B) En cuál turno los choferes son, en promedio, más jóvenes.
"""

"""def infoChoferes(edad, antiguedad, turno):
    edad = int(input("Ingrese la edad del chofer (25 a 40): "))
    if edad > 40 or edad < 25:
        print("Edad incorrecta. Ingrese una edad válida (25 a 40): ")"""
    
from utils import utils as u

def validarTurno():
    turno = str(input("Ingrese el turno ('M'|'T'|'N'): "))
    while turno not in ('M', 'T', 'N'):
        turno = str(input("Ingrese el turno ('M'|'T'|'N'): "))
    
    return turno

montoFinal = 0
montoParcial = 0
extra = 0

for i in range(3):
    edad = u.solicitarEnteroEntre(25, 40, "Ingrese la edad del chofer (25 a 40): ")
    antiguedad = u.solicitarEnteroEntre(5, 30, "Ingrese la antiguedad (5 a 30): ")
    turno = validarTurno()

    extra1 = 0
    extra2 = 0

    if antiguedad > (edad / 2):
        extra1 = 500 * 0.1
    
    if turno == 'N':
        extra2 = 500 * 0.05
    
    montoParcial = 500 + extra1 + extra2

    montoFinal += montoParcial

print(f"EL monto total de la empresa es de: {montoFinal}. ")















