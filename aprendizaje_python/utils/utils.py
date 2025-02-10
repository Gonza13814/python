"""En este archivo de python ponemos las funciones que suelen repetirse en los ejercicios para ahorrar codigo :) """

def solicitarEntero(mensaje):
   entero = int(input(mensaje))
   return entero

def solicitarFloat(mensaje):
   float = float(input(mensaje))
   return float

def solicitarEnteroEntre(valorMin, valorMax, mensaje):
    valor = int(input(mensaje))
    while valor not in range (valorMin, valorMax + 1):
       valor = int(input("ERROR. " + mensaje))
    
    return valor 

"""def solicitarString(mensaje):
   Solicita un string
   
def solicitarFloatEntre(valorMin, valorMax, mensaje):
    Solicita un float entre dos valores
    
def confirmarUsuario(mensaje):
    Un bucle que al poner S sigue Al poner N termina"""
   


