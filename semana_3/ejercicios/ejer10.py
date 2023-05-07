""" 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con todas las vocales en mayúscula. """

texto = input("Ingresar texto: ").lower()
texto_separado = []
texto_vocales_mayusculas = ""
vocales = "aeiou"

for letra in texto:
    texto_separado.append(letra)

i = 0
while i < len(texto_separado):
    if texto_separado[i] in vocales:
        texto_vocales_mayusculas += texto_separado[i].upper()
    else:
        texto_vocales_mayusculas += texto_separado[i]
    i += 1
print(f"Texto con vocales en mayusculas:\n{texto_vocales_mayusculas}")
