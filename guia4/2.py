"""2) obtenerResto, que devuelva el resto del
cociente entre dos números enteros dados
como parámetros (sin usar el operador %)."""

def obtenerResto(dividendo, divisor):
    cociente = dividendo // divisor  
    resto = dividendo - (cociente * divisor)
    return resto

print(obtenerResto(6,0))
    