""" 17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con las palabras en orden inverso. """

texto = input("Ingresar texto: ").lower().split(" ")[::-1]
texto_palabras_orden_inverso = " ".join(texto)
print(texto_palabras_orden_inverso)