""" 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
cuál de ellos es mayor. """

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

if numero1 > numero2:
    print(f"Es mayor el numero {numero1}")
elif numero2 > numero1:
    print(f"Es mayor el numero {numero2}")
else:
    print("Son iguales")
