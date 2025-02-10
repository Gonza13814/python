"""4) Realizá un programa que permita al usuario ingresar valores del mismo tipo para las variables a
y b. Una vez cargadas, la computadora debe mostrar ambas variables por pantalla, intercambiar
entre sí sus valores (que lo cargado en a quede en b, y viceversa), y volver a mostrarlas."""

variableA = int(input("Variable a: "))
variableB = int(input("Variable b: "))

print("Valores en orden de aparición: " + str(variableA) + " y " + str(variableB))

variableAux = variableA 
variableA = variableB
variableB = variableAux


print("Valores en orden inverso: " + str(variableA) +" y " + str(variableB))


