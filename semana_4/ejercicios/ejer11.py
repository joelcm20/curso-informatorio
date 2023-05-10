""" 11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene. """

def contar_vocales(texto):
    vocales = "aeiou"
    cantidad_vocales = 0
    for letra in texto:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

print(contar_vocales("qwrty"))