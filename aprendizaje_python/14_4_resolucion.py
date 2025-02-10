"""14) Realizá un programa que permita al usuario ingresar los datos de cada uno de los 8 choferes de 
una empresa de viajes en ómnibus: 
▪ Edad [25 a 40] ▪ Antigüedad [5 a 30] ▪ Turno ('M'|'T'|'N') 
Todos los choferes obtendrán un bono de 500 dólares. Los que tengan una antigüedad superior a la 
mitad de su edad, cobrarán un 10% extra. Los del turno nocturno cobrarán otro 5% extra.  
La computadora debe mostrar, de forma clara y ordenada:  
A)  El monto total que la empresa paga en concepto de bono para todos sus choferes. 
B)  En cuál turno los choferes son, en promedio, más jóvenes"""

from utils import utils as u

CANT_CHOFERES = 3
BONO_FIJO = 500

def main(cant, bonoFijo):
    montoTotal = 0
    turnoMasJoven = ''
    
    edadM, edadT, edadN = 0, 0, 0
    contM, contT, contN = 0, 0, 0
    
    """edades_por_turno = {'M': 0, 'N': 0, 'T': 0}
    """ 
    
    for i in range(cant):
        edad = u.solicitarEnteroEntre(25, 40, "Ingrese la edad del chofer entre 25 y 40: ")
        antiguedad = u.solicitarEnteroEntre(5, 30, "Ingrese la antiguedad entre 5 y 30: ")
        turno = validarTurno()
        
        montoParcial = calcularMontoParcial(edad, antiguedad, turno, bonoFijo)
        montoTotal += montoParcial
        
        if turno == 'M':
            edadM += edad
            contM += 1
        if turno == 'N':
            edadN += edad
            contN += 1
        if turno == 'T':
            edadT += edad
            contT += 1
        
        """edades_por_turno[turno] += edad
        """

    turnoMasJoven = calcularTurnoMasJoven(edadM, contM, edadN, contN,edadT, contT)
    print(f"El monto total es {montoTotal}")
    print(f"El turno con promedio de edad mas joven es {turnoMasJoven}")    

def calcularTurnoMasJoven(edadM, contM, edadN, contN,edadT, contT):
    promM = edadM / contM if contM > 0 else float('inf')
    promT = edadT / contT if contT > 0 else float('inf')
    promN = edadN / contN if contN > 0 else float('inf')
    
    if promM < promN and promM < promT:
        return 'M'
    elif promN < promT:
        return 'N'
    else:
        return 'T'

def calcularMontoParcial(edad, antiguedad, turno, bonoFijo):
    montoParcial = bonoFijo

    if antiguedad > (edad / 2):
        montoParcial *= 1.10

    if turno == 'N':
        montoParcial *= 1.05

    return montoParcial
        
def validarTurno():
    turno = str(input("Ingrese el turno ('M'|'T'|'N'): "))
    while turno not in ('M', 'T', 'N'):
        turno = str(input("Ingrese el turno ('M'|'T'|'N'): "))
    
    return turno

main(CANT_CHOFERES, BONO_FIJO)