""" 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial. """

caracter = input("Ingresar caracter: ")
if caracter.isupper():
    print("Es una letra mayuscula")
elif caracter.islower():
    print("Es una letra minuscula")
elif caracter.isnumeric():
    print("Es un numero")
else:
    print("Es un caracter especial")