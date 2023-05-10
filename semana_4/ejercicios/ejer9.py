""" 9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números. """


def promedio(lista_numeros):
    suma_total = sum(lista_numeros)
    return suma_total / len(lista_numeros)


print(promedio([6, 6, 6]))
