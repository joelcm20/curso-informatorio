""" 4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario. """

def es_capicua(numero):
    numero = str(numero)
    numero_invertido = numero[::-1]
    return numero == numero_invertido

print(es_capicua(121))