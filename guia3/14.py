"""14) Realizá un programa que permita al usuario ingresar personas (para cada una, la inicial de su
nombre y su edad). La carga termina cuando en la inicial del nombre de la persona se ingresa un
asterisco ('*'). La computadora debe indicar quién es la persona más joven."""

nombre = str(input("Ingrese la inicial del nombre de la persona: "))
edad = int(input("Ingrese la edad de la persona: "))
youngest = edad
nombreYoungest = nombre

while not nombre == "*":
    if (edad < youngest):
        youngest = edad
        nombreYoungest = nombre
    
    nombre = str(input("Ingrese la inicial del nombre de la persona: "))
    
    if nombre != "*":
        edad = int(input("Ingrese la edad de la persona: "))


print(f"La persona más joven es {nombreYoungest} con una edad de {youngest}")




