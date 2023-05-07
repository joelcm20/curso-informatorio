""" 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene. """

texto = input("Ingresar un texto: ")
palabras_de_texto = len(texto.split(" "))
print(f"El texto ingresado tiene {palabras_de_texto} palabras")
