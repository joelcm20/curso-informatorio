texto = input("- Ingresar un texto o frase cualquiera: ").lower()
print("- Tambien ingresa tres letras a tu eleccion.")
letra_1 = input("Letra 1: ").lower()
letra_2 = input("Letra 2: ").lower()
letra_3 = input("Letra 3: ").lower()

count_letra_1 = texto.count(letra_1)
count_letra_2 = texto.count(letra_2)
count_letra_3 = texto.count(letra_3)

count_palabras = len(texto.split(" "))
palabras_en_texto = {
    "python": "python" in texto
}

print(f"""
Cantidad de veces que aparecen las letras elegidas en el texto o frase.
- Letra {letra_1}: {count_letra_1}.
- Letra {letra_2}: {count_letra_2}.
- Letra {letra_3}: {count_letra_3}.

Datos del texto o frase.
- La cantidad de palabras: {count_palabras}.
- La primera letra es: {texto[0]}.
- La ultima letra es: {texto[len(texto)-1]}.
- El orden inverso: {texto[::-1]}.
- Palabras que aparecen:
    - python: {palabras_en_texto['python']}
""")