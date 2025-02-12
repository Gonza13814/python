"""14) Realizá un programa que permita al usuario ingresar los datos de cada uno de los 8 choferes de
una empresa de viajes en ómnibus:
▪ Edad [25 a 40] ▪ Antigüedad [5 a 30] ▪ Turno ('M'|'T'|'N')
Todos los choferes obtendrán un bono de 500 dólares. Los que tengan una antigüedad superior a la
mitad de su edad, cobrarán un 10% extra. Los del turno nocturno cobrarán otro 5% extra.
La computadora debe mostrar, de forma clara y ordenada:

A) El monto total que la empresa paga en concepto de bono para todos sus choferes.
B) En cuál turno los choferes son, en promedio, más jóvenes.
"""
from utils import utils as u

# A) El monto 0total que la empresa paga en concepto de bono para todos sus choferes.
CANT_CHOFERES = 1
turnoM = 0
turnoT = 0
turnoN = 0
edadM = 0
edadT = 0
edadN = 0
edadPromedioM = 100
edadPromedioT = 100
edadPromedioN = 100


def validarTurno():
    turno = str(input("Ingrese el turno ('M'|'T'|'N'): "))
    while turno not in ('M', 'T', 'N'):
        turno = str(input("Ingrese el turno ('M'|'T'|'N'): "))
    
    return turno

montoFinal = 0
montoParcial = 0

def calcularMontoParcial(edad, antiguedad, turno):
    montoAdicionalFinal = 500

    if antiguedad > (edad / 2):
        montoAdicionalFinal += 500 * 0.1
    
    if turno == 'N':
        montoAdicionalFinal += 500 * 0.05
    
    return montoAdicionalFinal

def encontrarTurnoConPromedioMasJoven(edadPromedioM, edadPromedioT, edadPromedioN):
    if edadPromedioM < edadPromedioT and edadPromedioM < edadPromedioN:
        return edadPromedioM, 'M'
    elif edadPromedioT < edadPromedioM and edadPromedioT < edadPromedioN:
        return edadPromedioT, 'T'
    elif edadPromedioN < edadPromedioT and edadPromedioN < edadPromedioM:
        return edadPromedioN, 'N'


for i in range(CANT_CHOFERES):
    edad = u.solicitarEnteroEntre(25, 40, "Ingrese la edad del chofer (25 a 40): ")
    antiguedad = u.solicitarEnteroEntre(5, 30, "Ingrese la antiguedad (5 a 30): ")
    turno = validarTurno()
    
    montoParcial = calcularMontoParcial(edad, antiguedad, turno)
    
    montoFinal += montoParcial

    if turno == 'M':
        turnoM += 1
        edadM += edad

    if turno == 'T':
        turnoT += 1
        edadT += edad

    if turno == 'N':
        turnoN += 1
        edadN += edad


edadPromedioM = edadM / turnoM if turnoM > 0 else float('inf')
edadPromedioT = edadT / turnoT if turnoT > 0 else float('inf')
edadPromedioN = edadN / turnoN if turnoN > 0 else float('inf')

print(f"El monto final es {montoFinal}. ")
#print(f"Los choferes mas jovenes estan en el turno {encontrarTurnoConPromedioMasJoven()}")
edadMasJovenYTurno = encontrarTurnoConPromedioMasJoven(edadPromedioM,edadPromedioT,edadPromedioN)
print(f"El turno con mas promedio joven es {edadMasJovenYTurno[1]} y es {edadMasJovenYTurno[0]}")
















