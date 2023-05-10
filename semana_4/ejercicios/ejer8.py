""" 8-Crea una función llamada es_palindromo que tome una cadena de texto como
parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
contrario. """


def es_palindromo(palabra):
    palabra_inversa = palabra[::-1]
    if palabra == palabra_inversa:
        return "Es polindromo"
    return "No es polindromo"

print(es_palindromo("jajajaja"))