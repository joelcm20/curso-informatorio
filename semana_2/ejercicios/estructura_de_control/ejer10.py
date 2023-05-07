""" 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante. """

letra = input("Ingresar una letra: ").lower()
vocales = "aeiou"

if vocales.find(letra) >= 0:
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante")