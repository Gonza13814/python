"""14) Realizá un programa que permita al usuario ingresar los datos de cada uno de los 8 choferes de 
una empresa de viajes en ómnibus: 
▪ Edad [25 a 40] ▪ Antigüedad [5 a 30] ▪ Turno ('M'|'T'|'N') 
Todos los choferes obtendrán un bono de 500 dólares. Los que tengan una antigüedad superior a la 
mitad de su edad, cobrarán un 10% extra. Los del turno nocturno cobrarán otro 5% extra.  
La computadora debe mostrar, de forma clara y ordenada:  
A)  El monto total que la empresa paga en concepto de bono para todos sus choferes. 
B)  En cuál turno los choferes son, en promedio, más jóvenes"""

from utils import utils as u

entero = u.solicitarEntero('nice: ')

print(entero)