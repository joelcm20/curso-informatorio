""" 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a". """

string = input("Ingresar un texto: ")
if string.find("a") == -1:
    print("El texto no contiene la letra \"a\"")
else:
    print("El texto contiene la letra \"a\" ")