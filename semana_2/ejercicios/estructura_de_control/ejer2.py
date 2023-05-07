""" 2-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero. """

entero = int(input("Numero entero: "))
if entero > 0:
    print("Numero positivo")
elif entero < 0:
    print("Numero negativo")
else:
    print("Numero es 0")