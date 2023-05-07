""" 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con cada palabra al revés. """

texto = input("Ingresar texto: ")
texto_a_lista = texto.split(" ")
palabras_reves = ""

for palabra in texto_a_lista:
    palabra_invertida = palabra[::-1]
    palabras_reves += f"{palabra_invertida} "

print(f"Texto con cada palabra al reves:\n{palabras_reves}")