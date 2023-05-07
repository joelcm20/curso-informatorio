""" 15-Escribe un programa que pida al usuario una cadena de texto y determine
cuántas veces aparece cada letra en la cadena. """

texto = input("Ingresar un texto: ").lower()
contador_letras = {}

for letra in texto:
    if letra != " ":
        if letra in contador_letras.keys():
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1

for key in contador_letras:
    print(f"- La letra {key} aparece {contador_letras[key]} veces.")
