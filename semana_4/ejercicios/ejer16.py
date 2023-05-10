""" 16-Crea una función llamada eliminar_duplicados que tome una lista como
parámetro y devuelva una nueva lista sin duplicados, conservando el orden
original. """


def eliminar_duplicados(lista):
    lista_nueva = []
    for elemento in lista:
        if not elemento in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva

print(eliminar_duplicados(["hola", "hola", "dos", "tres", "dos"]))