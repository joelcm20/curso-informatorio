""" 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
letras pero en distinto orden), o False en caso contrario. """


def es_anagrama(texto1, texto2):
    if texto1 == texto2 or not len(texto1) == len(texto2):
        return False
    for letra in texto1:
        if not letra in texto2:
            return False
    return True


print(es_anagrama("lhao", "hola"))
